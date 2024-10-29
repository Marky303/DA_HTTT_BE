import ast

def GetPromptContent(request):
    dict = request.body.decode("UTF-8")
    prompt = ast.literal_eval(dict)['prompt']
    return prompt