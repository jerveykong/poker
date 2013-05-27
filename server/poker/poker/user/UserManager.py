from poker.models.user import User

class UserManager:
    def addUser(self, uName):
        user = User()
        user.username = uName
        user.save()
