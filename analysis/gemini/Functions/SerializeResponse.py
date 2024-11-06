import json

def SerializeResponse(result):
    serializedResult = json_string = json.dumps(result)    
    return result