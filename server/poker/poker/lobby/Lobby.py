from poker.models.user import User

class Lobby:
    users=[];
#    tables=[];
    def __init__(self):
        self.users = [{'username':'foo'}, {'username':'bar'}]
    def loadLobby(self):
        self.users = User.objects.all()
    def getUsers(self):
        return self.users
