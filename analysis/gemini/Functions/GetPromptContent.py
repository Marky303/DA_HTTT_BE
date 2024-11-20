import json

def GetPromptContent(request):
    dict = request.body.decode("UTF-8")
    # dict = dict.replace("null", "None")
    prompt = json.loads(dict)['prompt']
    return prompt