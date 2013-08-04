from django.http import HttpResponse
import json

from poker.base.common.ErrorCodes import ResponseErrorCode

# Base Json HTTP Response
class JsonHttpResponse(HttpResponse):
    def __init__(self, response):
        return HttpResponse.__init__(self, json.dumps(response), "application/json")

# Success Json HTTP Response
class JsonHttpSuccessResponse(JsonHttpResponse):
    def __init__(self, response):
        jsonResponse = {"result" : True}
        jsonResponse.update(response);
        return JsonHttpResponse.__init__(self, jsonResponse)

# Invalid Method Json HTTP Response
class JsonHttpInvalidRequest(JsonHttpResponse):
    def __init__(self, message):
        jsonResponse = {"result" : False, "errorNo": ResponseErrorCode.INVALID_REQUEST, "error": "Invalid Request", "errorMessage": message}
        return JsonHttpResponse.__init__(self, jsonResponse)
