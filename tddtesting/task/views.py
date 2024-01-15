from django.shortcuts import render

from .models import Task
from django.views import View

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt


from .forms import NewTaskForm



# Create your views here.
class Index(View) :    

    def get(self, request, *args, **kwargs) :
        print(kwargs) #/task/<int:pk> in here        
        
        tasks = Task.objects.all()
        return render(request, 'task/index.html', {'tasks' : tasks})

class Detail(View) :
    def get(self, request, *args, **kwargs) :
        task = Task.objects.get(pk=kwargs["pk"])
        return render(request, 'task/detail.html', {'task' : task})



class AAA(View) :
    # @csrf_exempt
    def get(self, request, *args, **kwargs) :
        form = NewTaskForm()
        return render(request, 'task/new.html', {"form" : form})