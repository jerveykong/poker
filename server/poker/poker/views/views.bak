from django.http import HttpResponse
import poker.lobby.Lobby

def index(request):
    lobby = poker.lobby.Lobby.Lobby()
    users = lobby.loadLobby()
    users = lobby.getUsers()
    print "users are " + str(users)
    results = ""
    for x in users:
        results += str(x.username) + " ";
    return HttpResponse("Hello, world." + results)
