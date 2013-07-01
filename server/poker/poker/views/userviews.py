
from django.template import Context, loader
from django.views.decorators.csrf import csrf_exempt

from poker.base.common.Common import *
from poker.user.UserManager import UserManager

@csrf_exempt
def index(request):
    try:
        userManager = UserManager()
        if( request.method == 'PUT' ):
            body = json.loads(request.read())
            userManager.addUser(body)
            response = {"success": "User has been added"}
            result = True

            traceLogger.debug("Adding user success")
        else:
            return JsonHttpInvalidMethod()
    except BaseException, e:
        errorLogger.error(e)
        result = False
        response = {"failure": "An error has occured"}

    return JsonHttpSuccessResponse(response);
