from django.shortcuts import render

# Create your views here.
def index_page_view(request):
    data = {
        "show_data" : False,
        "name" : "Ishjot",
        "course" : "Python Backend Development live",
        "list" : [1, 2, 3, 4]
    }
    return render(request, "index.html", context=data)
    