from rest_framework import serializers

from todo.models import Todo

class TodoSerializer(serializers.ModelSerializer):
    """  This is a class of serializer for todo modal.  """
    class Meta:
        model = Todo
        fields = ('id', 'title', 'description',
                  'completed', 'reminder_datatime')
