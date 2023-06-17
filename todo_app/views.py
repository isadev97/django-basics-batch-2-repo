from django.shortcuts import render, redirect
from django.http import HttpResponse
from todo_app.models import Todo

# Create your views here.
def list_view(request):
    print(request.method)
    search_string = request.GET.get('search', "")
    todo_list = Todo.objects.all().order_by("-created_at")
    if search_string != "":
        todo_list = todo_list.filter(title__istartswith=search_string)
    data = {
        "todo_list" : todo_list
    }
    return render(request, "list.html", context=data)

def create_view(request):
    todo_title = request.POST['todoTitle']
    todo_desc = request.POST['todoDescription']
    Todo.objects.create(
        title=todo_title,
        description=todo_desc,
        completed=False
    )
    return redirect("todo_list_view")

def update_view(request, todo_id):
    if request.method != "POST":
        return HttpResponse("Error method not allowed")
    else:
        todo = Todo.objects.get(id=todo_id)
        todo.completed = True
        todo.save()
        return redirect("todo_list_view")

def delete_view(request, todo_id):
    if request.method != "POST":
        return HttpResponse("Error method not allowed")
    else:
        todo = Todo.objects.get(id=todo_id)
        todo.delete()
        return redirect("todo_list_view")