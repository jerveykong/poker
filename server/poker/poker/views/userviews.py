from django.template import Context, loader
from django.views.decorators.csrf import csrf_exempt

from poker.base.common.Common import *
from poker.controllers.user import UserController
from poker.models.user import User

@csrf_exempt
def index(request):
    try:
        userController = UserController()

        if( request.method == 'PUT' ):
            body = json.loads(request.read())

            userController.addUser(body)
            response = {"success": "User has been added"}
            traceMessage = "Adding user success"
        elif( request.method == 'GET' ):
            user            = userController.getUser(request.REQUEST)
            modelSerializer = ModelSerializer()
            userSerialized  = modelSerializer.serializeOne(user)

            response = {"success": {"user": userSerialized}}
            traceMessage = "User has been fetched -- userId: " + str(user.id) + " details: " + str(userSerialized)
        else:
            return JsonHttpInvalidRequest()

    except InvalidRequestException, e:
        traceLogger.debug(e)
        return JsonHttpInvalidRequest("Key error " + str(e));

    except BaseException, e:
        errorLogger.exception(e)
        traceMessage = e;
        response = {"failure": "An error has occured"}

    traceLogger.debug(traceMessage)
    return JsonHttpSuccessResponse(response);
