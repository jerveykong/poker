from poker.models.user import User

class UserManager:
    def addUser(self, body):
        user = User()
        user.username = body['username']
        user.save()
