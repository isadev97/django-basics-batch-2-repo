from django.shortcuts import render

# Create your views here.
def index_page_view(request):
    data = {
        "name" : "Ishjot",
        "course" : "Python Backend Development live"
    }
    return render(request, "index.html", context=data)
    