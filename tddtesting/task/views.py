from django.shortcuts import render

from .models import Task
from django.views import View

# Create your views here.
class TTTT(View) :    

    def get(self, request, *args, **kwargs) :
        print(kwargs)
        print(args)
        
        tasks = Task.objects.all()
        return render(request, 'task/index.html', {'tasks' : tasks})

    def detail(self, request, pk) :
        task = Task.objects.get(pk=pk)
        return render(request, 'task/detail.html', {'task' : task})

    def new(self, request) :
        return render(request, 'task/new.html')