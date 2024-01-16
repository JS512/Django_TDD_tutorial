from django.urls import path
from task.views import Index, Detail, AAA, Update, Delete

from . import views

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('<int:pk>/', Detail.as_view(), name="detail"), 
    path('new/', AAA.as_view(), name='new'),
    path('<int:pk>/update/', Update.as_view(), name='update'),
    path('<int:pk>/delete/', Delete.as_view(), name='delete'),
     
]