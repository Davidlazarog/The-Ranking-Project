from flask import request, Response
from bson import json_util
import json
def json_response_lab(data):
    """
    Process data with bson serializer to avoid ObjectID to string errors in flask
    """
    return Response(
        json_util.dumps(data),
        mimetype='application/json'
    )
def asJsonResponseLabs(fn):
    """
    Decorator to process data with bson serializer to avoid ObjectID to string errors in flask
    """
    def wrapperLab(*args, **kwargs):
        data = fn(*args, **kwargs)
        if isinstance(data, tuple):
            return json_response_lab(data[0]),data[1]
        else:
            return json_response_lab(data)
    return wrapperLab