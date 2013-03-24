from django.http import HttpResponse
from echo.models import User

def index(request):
    u = User(firstname=request.GET["fname"], lastname=request.GET["lname"])
    u.save();
    return HttpResponse("Hello, world." + str(request.GET.dict()))

def getUser(request):
    users = User.objects.filter(lastname = request.GET["lastname"]);
    results = "results: "; 
    for u in users:
        results += str(u) + " ";
    return HttpResponse(results);
