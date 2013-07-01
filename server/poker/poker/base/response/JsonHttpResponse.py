from django.http import HttpResponse
import json

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
class JsonHttpInvalidMethod(JsonHttpResponse):
    def __init__(self):
        jsonResponse = {"result" : False, "errorNo": 1000, "error": "Invalid Request"}
        return JsonHttpResponse.__init__(self, jsonResponse)
