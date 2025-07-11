from rest_framework.serializers import ModelSerializer
from .models import Task

class TaskSerializer(ModelSerializer):
    class Meta:
        model = Task
        fields =['title']

class TaskDetailsSerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"


