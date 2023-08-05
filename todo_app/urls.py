from django.urls import path
from todo_app.views import list_view, create_view, update_view, delete_view, DRFListView, DRFCreateView, DRFDeleteView

urlpatterns = [
    path("list/", list_view, name="todo_list_view"),
    path("create/", create_view, name="todo_create_view"),
    path("update/<int:todo_id>/", update_view, name="todo_update_view"),
    path("delete/<int:todo_id>/", delete_view, name="todo_delete_view"),
    path("drf/list", DRFListView.as_view(), name="drf_todo_list"),
    path("drf/create", DRFCreateView.as_view(), name="drf_todo_create"),
    path("drf/delete", DRFDeleteView.as_view(), name="drf_todo_delete")
]
