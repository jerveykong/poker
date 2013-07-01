from poker.models.user import User
from poker.models.table import Table

class Lobby:
    users   = [];
    tables  = [];
    def loadLobby(self):
        self.users  = User.objects.all()
        self.tables = Table.objects.all()

    def getUsers(self):
        return self.users
    def getTables(self):
        return self.tables
