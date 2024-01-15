from django.urls import path
from task.views import Index, Detail, AAA

from . import views

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('<int:pk>/', Detail.as_view(), name="detail"), 
    path('new/', AAA.as_view(), name='new'),
     
]