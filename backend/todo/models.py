from django.db import models

class Todo(models.Model):
  ''' model for todo app '''
  title = models.CharField(max_length=120)
  description = models.TextField()
  completed = models.BooleanField(default=False)
  reminder_datatime = models.DateTimeField(auto_now = False)
      
  def __str__(self):
    return self.title