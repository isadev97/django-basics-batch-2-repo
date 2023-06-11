from django.urls import path
from todo_app.views import list_view, update_view, delete_view

urlpatterns = [
    path("list/", list_view, name="todo_list_view"),
    path("update/<int:todo_id>/", update_view, name="todo_update_view"),
    path("delete/<int:todo_id>/", delete_view, name="todo_delete_view")
]
