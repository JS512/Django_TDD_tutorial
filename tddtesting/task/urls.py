from django.urls import path
from task.views import TTTT
from . import views

urlpatterns = [
    path('', TTTT.as_view(), name='index'),
    path('new/', TTTT.as_view(), name='new'),
    path('<int:pk>/', TTTT.as_view(), name="detail")   
]