from . import views
from django.contrib import admin
from django.urls import path
app_name='web'
urlpatterns = [
    path('',views.demo,name='demo'),
    path('movie/<int:taskid>/',views.detail,name='detail'),
    path('add/',views.add,name='add'),
    path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:id>/',views.delete,name='delete')

]