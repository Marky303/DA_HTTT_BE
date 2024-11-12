import time

# Import functions
from analysis.gemini.Functions.GetPromptContent import GetPromptContent
from analysis.gemini.Functions.GenerateResponse import *

# Call functions
from analysis.gemini.QueryGraphAnalysis import Query, Graph

# Process the prompt and return a JSON analysis result object
def GeminiController(request):
    # Record start time
    start_time = time.time()
    
    # Get user prompt content
    prompt          = GetPromptContent(request)
    
    # Generate response from gemini
    response        = GenerateInitialResponse(prompt)
    
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
            queryResult         = Query(fc.args['query'])
            result['list'].append(queryResult)
            
            # Explain the query... like bruh
            queryExplainResult  = GenerateQueryExplaination(queryResult['query'])
            result['list'].append(queryExplainResult)
            
            # Get the graph type
            graphType           = GenerateGraphType(queryResult['query'])
            
            # Draw graphs and append the graph to the final result
            Graph(graphType, queryResult['data'], result)
            
            # # Get some sort of overview and append to the final result??
            # graphExplainResult  = GenerateGraphExplaination(graphResult)
            
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
    
    # Calculate elapsed time
    end_time = time.time()  # Record the end time
    elapsed_time = end_time - start_time
    
    # Create a text and append to the final result
    elapsedResponse = {
        "type": "elapsedTime",
        "content": "Elapsed time: " + str(elapsed_time)
    }
    result['list'].append(elapsedResponse)
    
    # Return a dictionary
    return result
    
    