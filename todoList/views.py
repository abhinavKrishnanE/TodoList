from django.shortcuts import render
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from .serializer import TaskSerializer, TaskDetailsSerializer
from .models import Task
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q, Count
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from django.db import connection


class ListTaks(ListCreateAPIView):

    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ["^title","^description"]
    print(Task.objects.annotate(task_count = Count('title')))

    def get_queryset(self):
        task_count_obj = Task.objects.annotate(task_count = Count('title'))
        for task in task_count_obj:
            print(task.task_count)
        return Task.objects.filter(owner=self.request.user) 




class ListTaskDetails(RetrieveUpdateDestroyAPIView):
    def get_queryset(self):
        return Task.objects.filter(owner=self.request.user)    
    serializer_class = TaskDetailsSerializer
    permission_classes = [IsAuthenticated]


    
    # queryset = Task.objects.filter(owner=self.request.user)
    #     new_queryset = queryset
    #     search = self.request.query_params.get('search')
    #     status = self.request.query_params.get('status')
    #     if search is not None:
    #         if status is None:
    #             queryset = new_queryset.filter(Q(title__istartswith = search) | Q(description__istartswith = search))
    #         else:
    #             queryset = new_queryset.filter((Q(title__istartswith = search) | Q(description__istartswith = search)), status__icontains = status)
    #     elif status is not None:
    #             queryset = new_queryset.filter(status__icontains = status)
    #     return queryset
    # queryset = Task.objects.filter(owner=self.request.user)
        # new_queryset = queryset
        # search = self.request.query_params.get('search')
        # status = self.request.query_params.get('status')
        # if search is not None:
        #     if status is None:
        #         queryset = new_queryset.filter(Q(title__istartswith = search) | Q(description__istartswith = search))
        #     else:
        #         queryset = new_queryset.filter((Q(title__istartswith = search) | Q(description__istartswith = search)), status__icontains = status)
        # elif status is not None:
        #         queryset = new_queryset.filter(status__icontains = status)
        # return queryset
