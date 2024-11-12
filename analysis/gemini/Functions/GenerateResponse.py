# Import libraries
import os
from dotenv import load_dotenv
import google.generativeai as genai
from PIL import Image
from django.conf import settings
from enum import Enum

# GEMINI RELATED___________________________________________________________
def QueryPostgresDatamart(query: str):
    """Create a Postgres query as parameter to query the infomation asked by the user in the Postgres datamart. The function will search the postgres database using the query and return the user the table result. After that, the function will draw a graph based on the graphType parameter. For bar graph and pie graph, the first column of the result in the query MUST be categories or labels (the x axis). For line graph, the first column (usually a date column) is the x axis.
    Args:
        query: Create a query that will be queried in the Postgres datamart. The query must be on a single line. Only generate the syntatically correct and bare query, without any newline or other special characters. You can rename the columns of the query result to match the content. 
    Returns:
        The result of the query (and maybe a graph)
    """
    return []

class Graph(Enum):
    BAR = 'bar'
    LINE = 'line'
    # PIE = 'pie'
    NONE = 'none'

def DrawGraph(graphType: Graph):
    """Draw a graph based on the user's query
    Args:
        graphType: Choose a suitable graph type that can present the data result of the user's query. "none" should only be your answer when there is no graph that can be used to present the result data
    Returns:
        Draw a graph for the user's query
    """
    return []

# Generate response from gemini
def GenerateInitialResponse(prompt):
    load_dotenv()
    
    try:
        # Get system instruction
        instructionFilePath     = str(settings.BASE_DIR) + "\\analysis\\gemini\\templates\\InstructionTemplate.txt"
        instructionFile         = open(instructionFilePath) 
        instruction             = instructionFile.read()

        # Create model object
        genai.configure(api_key=os.getenv("GOOGLE_AI_API_KEY"))
        model = genai.GenerativeModel(
            model_name="gemini-1.5-flash",
            tools=[QueryPostgresDatamart],
            system_instruction=instruction
        )

        # TEST        
        # print(model._tools.to_proto())
        
        # Generate response
        chat = model.start_chat()
        response = chat.send_message(prompt)
        
        return response
            
    except Exception as e:
        # Notify
        print(f"An error occurred when generating response: {e}")
        return None
    
    
# Generate explaination for the query
def GenerateQueryExplaination(query):
    load_dotenv()
    
    try:
        # Get system instruction
        instructionFilePath     = str(settings.BASE_DIR) + "\\analysis\\gemini\\templates\\InstructionTemplate.txt"
        instructionFile         = open(instructionFilePath) 
        instruction             = instructionFile.read()

        # Create model object
        genai.configure(api_key=os.getenv("GOOGLE_AI_API_KEY"))
        model = genai.GenerativeModel(
            model_name="gemini-1.5-flash",
            system_instruction=instruction
        )

        # Get prompt
        queryExplainPromptFilePath  = str(settings.BASE_DIR) + "\\analysis\\gemini\\templates\\QueryExplainationPrompt.txt"
        queryExplainPromptFile      = open(queryExplainPromptFilePath) 
        queryExplainPrompt          = queryExplainPromptFile.read()
        
        queryExplainPrompt          = queryExplainPrompt.replace("<query>", query)
        
        # Generate response
        chat = model.start_chat()
        response = chat.send_message(queryExplainPrompt)
        
        # Create result dict
        textResponse = {
            "type": "text",
            "content": response.text
        }
        
        return textResponse
            
    except Exception as e:
        # Notify
        print(f"An error occurred when generating response: {e}")
        return None
    
# Generate graph type from Gemini
def GenerateGraphType(query):
    load_dotenv()
    
    try:
        # Get system instruction
        instructionFilePath     = str(settings.BASE_DIR) + "\\analysis\\gemini\\templates\\InstructionTemplate.txt"
        instructionFile         = open(instructionFilePath) 
        instruction             = instructionFile.read()

        # Create model object
        genai.configure(api_key=os.getenv("GOOGLE_AI_API_KEY"))
        model = genai.GenerativeModel(
            model_name="gemini-1.5-flash",
            tools=[DrawGraph],
            system_instruction=instruction
        )

        # Get prompt
        graphTypePromptFilePath  = str(settings.BASE_DIR) + "\\analysis\\gemini\\templates\\GraphTypeTemplate.txt"
        graphTypePromptFile      = open(graphTypePromptFilePath) 
        graphTypePrompt          = graphTypePromptFile.read()
        
        graphTypePrompt          = graphTypePrompt.replace("<query>", query)
        
        # Generate response
        chat = model.start_chat()
        response = chat.send_message(graphTypePrompt)
        
        # Return    
        return response
            
    except Exception as e:
        # Notify
        print(f"An error occurred when generating response: {e}")
        return None
    
# Generate graph overview from gemini
def GenerateGraphOverview(data, buffer):
    load_dotenv()
    
    try:
        # Get system instruction
        instructionFilePath     = str(settings.BASE_DIR) + "\\analysis\\gemini\\templates\\InstructionTemplate.txt"
        instructionFile         = open(instructionFilePath) 
        instruction             = instructionFile.read()

        # Create model object
        genai.configure(api_key=os.getenv("GOOGLE_AI_API_KEY"))
        model = genai.GenerativeModel(
            model_name="gemini-1.5-flash",
            system_instruction=instruction
        )

        # Get prompt
        graphOverviewPromptFilePath  = str(settings.BASE_DIR) + "\\analysis\\gemini\\templates\\GraphOverviewTemplate.txt"
        graphOverviewPromptFile      = open(graphOverviewPromptFilePath) 
        graphOverviewPrompt          = graphOverviewPromptFile.read()
        
        graphOverviewPrompt          = graphOverviewPrompt.replace("<data>", str(data))
        
        # Get image
        image = Image.open(buffer)
        
        # Generate response
        response = model.generate_content(
            [graphOverviewPrompt, "\n\n", image]
        )
        
        # Return    
        return response.text
            
    except Exception as e:
        # Notify
        print(f"An error occurred when generating response: {e}")
        return None