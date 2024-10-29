import ast

# Import functions
from analysis.gemini.Functions.GetPromptContent import GetPromptContent
from analysis.gemini.Functions.GenerateResponse import GenerateResponse

# Call functions
from analysis.gemini.QueryGraphAnalysis import Query, Graph

# Process the prompt and return a JSON analysis result object
def GeminiController(request):
    # Get user prompt content
    prompt          = GetPromptContent(request)
    
    # Generate response from gemini
    response        = GenerateResponse(prompt)
    
    # Define the final result
    result = {
        "list": []
    }
    
    # Handle response cases
    fc = response.candidates[0].content.parts[0].function_call
    # Check if response has function call
    if fc:
        
        # Check if it is a query function
        if fc.name == "QueryPostgresDatamart":
            # Query and append query result to the final result
            queryResult     = Query(fc.args['query'])
            result['list'].append(queryResult)
            
            # Draw a graph and append the graph to the final result???
            graphResult     = Graph(fc.args['graphType'], fc.args['graphName'])
            
            
            # Get some sort of overview and append to the final result??
            
            
        # Check if it is an analysis function
        elif fc.name == "DeezNut":
            # TODO
            pass 
        
    else:
        # Create a text and append to the final result
        textResponse = {
            "type": "text",
            "content": response.text
        }
        result['list'].append(textResponse)
    
    # Return a dictionary
    return result
    
    