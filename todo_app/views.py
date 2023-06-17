from django.shortcuts import render, redirect
from django.http import HttpResponse
from todo_app.models import Todo

# Create your views here.
def list_view(request):
    search_string = request.GET.get('search', "")
    order_by_oldest = request.GET.get("order_by_oldest", "") == "true"
    order_by_latest = request.GET.get("order_by_latest", "") == "true"
    status_mapping = {
        'incomplete' : False,
        'complete' : True
    }
    status = request.GET.get('status', "")
    todo_list = Todo.objects.all().order_by("-created_at")
    if search_string != "":
        todo_list = todo_list.filter(title__istartswith=search_string)
    if status != "":
        status_in_boolean = status_mapping[status]
        todo_list = todo_list.filter(completed=status_in_boolean)
    if order_by_oldest:
        todo_list = todo_list.order_by("created_at")        
    if order_by_latest:
        todo_list = todo_list.order_by("-created_at")
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