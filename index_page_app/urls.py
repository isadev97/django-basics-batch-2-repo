from django.urls import path
from index_page_app.views import index_page_view

urlpatterns = [
    path("", index_page_view),
]
