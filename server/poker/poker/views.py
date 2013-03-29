from django.http import HttpResponse
import poker.lobby.Lobby

def index(request):
    lobby = poker.lobby.Lobby.Lobby()
    users = lobby.getUsers()
    print users
    results = ""
    for key,value in users:
        print x
        #results += str(value) + " ";
    return HttpResponse("Hello, world." + results)
    return HttpResponse("Hello, world.")
