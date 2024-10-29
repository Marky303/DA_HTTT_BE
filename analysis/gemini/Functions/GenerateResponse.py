# Import libraries
import os
from dotenv import load_dotenv
import google.generativeai as genai
from django.conf import settings

# Call functions
from analysis.gemini.CallFunctions.QueryGraphAnalysis import QueryPostgresDatamart


# Generate response from gemini
def GenerateResponse(prompt):
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

        # # Get response object
        # responseObject = response._result.candidates[0].content
        
        return response
            
    except Exception as e:
        # Notify
        print(f"An error occurred when generating response: {e}")
        return None