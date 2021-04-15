from datetime import datetime
from datetime import datetime, timedelta

from django.http import Http404
from django.shortcuts import render
from django.http.response import JsonResponse
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.utils.html import strip_tags

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework import mixins
from rest_framework.views import APIView

from todo import task
from todo.models import Todo
from todo.serializers import TodoSerializer


class TodoView(viewsets.ModelViewSet):
    ''' class for serializer'''
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()


class Summary(APIView):
    ''' this function will mail summery of todo task'''

    def post(self, request):
        try:
            data = request.data
            tasks = Todo.objects.filter(
                reminder_datatime__date=data['reminder_datatime'][0:10])
            meta_data={
                'data':tasks
            }
            text_content=render_to_string("email_body.txt",meta_data)
            task.duplicate_send_f_gmail.apply_async(
                ('summery', text_content, str(data['reminder_datatime'][8:])))
            return JsonResponse({"status": "done"})

        except Exception as e:
            return JsonResponse({"status": "fail", "reason": str(e)})


class AddTask(APIView):
    '''this function will add new task '''
    def post(self, request, format=None):
        serializer = TodoSerializer(data=request.data)
        data = request.data
        if serializer.is_valid():
            serializer.save()
            task.send_f_gmail.apply_async((data['title'], data['description']), eta=data['reminder_datatime'])
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
