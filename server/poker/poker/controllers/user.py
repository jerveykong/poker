from poker.base.common.Common import *
from poker.models.user import User

class UserController:
    def addUser(self, body):
        #Validate the request
        if( 'username' not in body ):
            raise InvalidRequestException('username key missing')

        userModel = User()
        userModel.manager.addUser(body['username'])
    def getUser(self, request):

        #Validate the request
        if( 'userId' not in request ):
            raise InvalidRequestException('userId key missing')

        userId  = request['userId']

        userModel = User()
        user = userModel.manager.getUser(userId)
        return user
