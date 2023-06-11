from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index_view(request):
    response = """ 
    <h1>response</h1>
    <h1>hello</h1>
    <h1>world</h1>
    """
    return HttpResponse(response)