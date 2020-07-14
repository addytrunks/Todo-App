from django.shortcuts import render
from .models import Todo
from .forms import TodoForm,UpdateTodoForm
from django.http import HttpResponseRedirect
from django.views.generic import UpdateView
from django.contrib import messages

# Create your views here.
def home(request):
    todos = Todo.objects.order_by('-created_at')
    todo_count = todos.count()
    completed = Todo.objects.filter(completed=True).count()
    not_completed = Todo.objects.filter(completed=False).count()

    if request.method == 'POST':
        todo_form = TodoForm(request.POST)
        todoop = request.POST.get('todo')
        if todo_form.is_valid():
            if Todo.objects.filter(todo=todoop).count() == 0:
                todo_form.save()
                messages.success(request,('Todo has been added successfully added to your list'))
            else:
                messages.error(request,('You have already added "{}" to your list'.format(todoop)))
    todo_form = TodoForm()

    return render(request,'home.html',context={'todos':todos,'form':todo_form,'todo_count':todo_count
    ,'completed':completed,'not_completed':not_completed,})

def delete(request,pk):
    todo = Todo.objects.get(id=pk)
    todoop = request.POST.get('todo')

    if request.method =='POST':
        todo.delete()
        messages.success(request,('Item  has been successfully deleted from your list.'))
        return HttpResponseRedirect('/')

    return render(request,'delete.html',context={'todo':todo})

class UpdateTodo(UpdateView):
    model = Todo
    form_class = UpdateTodoForm
    template_name = 'update.html'