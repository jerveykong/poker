import json

from django.core import serializers
from django.http import HttpResponse
from django.template import Context, loader
from poker.lobby.Lobby import Lobby

def index(request):
    lobby = Lobby()
    lobby.loadLobby()

    users   = lobby.getUsers()
    userOutput = []
    for x in users:
        userOutput.append({'username': x.username})

    tables  = lobby.getTables()
    tableOutput=[]
    for x in tables:
        tableOutput.append({'name': x.name})

    output = {}
    output['users']     = userOutput
    output['tables']    = tableOutput

    template = loader.get_template('poker/index.html');
    context = Context({'output': json.dumps(output)});

    #return HttpResponse("Hello, world." + results)
    return HttpResponse(template.render(context));
