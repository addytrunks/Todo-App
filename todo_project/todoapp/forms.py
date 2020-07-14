from django.forms import ModelForm,TextInput,Select
from .models import Todo

class TodoForm(ModelForm):
    class Meta():
        model = Todo
        fields = ['todo']

        widgets = {
            'todo':TextInput(attrs={'class':'form-control','placeholder':'Enter a Todo.....'}),
        }

class UpdateTodoForm(ModelForm):
    class Meta():
        model = Todo
        fields = ['todo','completed']

        widgets ={
            'todo':TextInput(attrs={'class':'form-control'}),
        }