from django.core.exceptions import *

class ModelAttributeException(Exception):
    def __init__(self, message):

        # Call the base class constructor with the parameters it needs
        Exception.__init__(self, message)
