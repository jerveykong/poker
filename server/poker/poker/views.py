from django.http import HttpResponse
from lobby import Lobby

def index(request):
    l = Lobby;
#    l.loadLobby();
    for x in l.getUsers():
        results += str(x.username) + " ";
    return HttpResponse("Hello, world." + results)
