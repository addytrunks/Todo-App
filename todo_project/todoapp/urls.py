from django.urls import path
from todoapp import views

urlpatterns = [
    path('',views.home,name='home'),
    path('delete/<int:pk>',views.delete,name='delete'),
    path('update/<int:pk>',views.UpdateTodo.as_view(),name='update'),
]
