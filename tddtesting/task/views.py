from django.shortcuts import render, redirect

from .models import Task
from django.views import View

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt


from .forms import NewTaskForm, UpdateTaskForm



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
    @csrf_exempt
    def get(self, request, *args, **kwargs) :
        form = NewTaskForm()
        return render(request, 'task/new.html', {"form" : form})

    def post(self, request, *args, **kwargs) :        
        form = NewTaskForm(request.POST)
        
        if form.is_valid() :
            form.save()

            return redirect('/')

        return render(request, 'task/new.html', {"form" : form})
    


class Update(View) :
    @csrf_exempt
    def get(self, request, *args, **kwargs) :
        task = Task.objects.get(pk=kwargs["pk"])
        return render(request, 'task/update.html', {'task' : task})
    
    def post(self, request, *args, **kwargs) :
        
        task = Task.objects.get(pk=kwargs["pk"])
        form = UpdateTaskForm(request.POST, instance=task)

        if form.is_valid() :
            form.save()

            return redirect('/')
        return render(request, 'task/update.html', {'task' : task, 'form' : form})
    

class Delete(View) :
    @csrf_exempt
    def get(self, request, *args, **kwargs) :
        task = Task.objects.get(pk=kwargs["pk"])
        task.delete()
        
        return redirect('/')
        
