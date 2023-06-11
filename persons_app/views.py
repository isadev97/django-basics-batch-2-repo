from django.shortcuts import render
from persons_app.models import Person
from django.http import HttpResponse, JsonResponse


# Create your views here.
def index_view(request):
    response = """ 
    <h1>response</h1>
    <h1>hello</h1>
    <h1>world</h1>
    """
    return HttpResponse(response)

def person_detail_view(request, person_id):
    try:
        person_object = Person.objects.get(pk=person_id)
    except Person.DoesNotExist:
        return JsonResponse({"error" : True, "message" : "Person Does not exist", "status" : 404})
    return JsonResponse({
        "id": person_object.id,
        "name": person_object.name,
        "age": person_object.age,
        "status": 200
    })