from django.contrib import admin
from django.urls import path, include
from.import views

urlpatterns = [
    path('',views.add,name='add'),
    path('delete/<int:featherid>/',views.delete,name='delete'),
    path('update/<int:id>/',views.update,name='update')
]
