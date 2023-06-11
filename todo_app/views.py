from django.shortcuts import render, redirect
from todo_app.models import Todo

# Create your views here.
def list_view(request):
    data = {
        "todo_list" : Todo.objects.all().order_by("-created_at")
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
    pass 

def delete_view(request, todo_id):
    pass