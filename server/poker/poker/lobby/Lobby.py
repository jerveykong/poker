from poker.models import User

class Lobby:
#    users=[];
#    tables=[];

    def __init__(self):
#        self.users = [];
        self.users = {'username':"foo", 'username':"bar"};
        self.tables = [];
        print 'are we __init__ing?';

    def loadLobby(self):
        self.users = User.objects.all();

    def getUsers():
        return users;
