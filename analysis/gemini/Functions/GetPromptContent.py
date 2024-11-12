import ast

def GetPromptContent(request):
    dict = request.body.decode("UTF-8")
    dict = dict.replace("null", "None")
    prompt = ast.literal_eval(dict)['prompt']
    return prompt