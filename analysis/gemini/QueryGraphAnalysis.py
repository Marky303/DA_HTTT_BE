import os
from dotenv import load_dotenv
import re
from enum import Enum
import psycopg
load_dotenv()

# GEMINI RELATED___________________________________________________________
# Define enum type
class Graph(Enum):
    BAR = 'bar'
    LINE = 'line'
    PIE = 'pie'
    NONE = 'none'

def QueryPostgresDatamart(query: str, graphType: Graph, graphName: str):
    """Create a Postgres query as parameter to query the infomation asked by the user in the Postgres datamart. The function will search the postgres database using the query and return the user the table result. After that, the function will draw a graph based on the graphType parameter. For bar graph and pie graph, the first column of the result in the query MUST be categories or labels (the x axis). For line graph, the first column (usually a date column) is the x axis.
    Args:
        query: Create a query that will be queried in the Postgres datamart. The query must be on a single line. Only generate the syntatically correct and bare query, without any newline or other special characters. You can rename the columns of the query result to match the content. 
        graphType: The type of graph that the function will draw after querying the result. graphType is of enum(string) type. ONLY CHOOSE "none" WHEN THE DATA CANNOT BE DESCRIBED IN THESE GRAPHS.
        graphName: The name of the graph that the function will draw. If the graphType is "none", the graph name will also be "none".
    Returns:
        The result of the query (and maybe a graph)
    """
    return []


# QUERY RELATED____________________________________________________________
# Preprocessing the query
fieldNames = [
    "OrderDate",
    "SubTotal",
    "TaxAmt",
    "Freight",
    "TotalDue",
    "Employee_id",
    "Customer_id",
    "OrderQty",
    "LineTotal",
    "Product_id",
    "SpecialOffer_id",
    "SalesOrder_id",
    "Name",
    "ListPrice",
    "StandardCost",
    "DiscountPct",
    "IndividualName",
    "StoreName",
    "Territory_id",
    "Group",
    "id",
]

def PreprocessQuery(query):
    # Add quotation mark
    for fieldName in fieldNames:
        query = re.sub(rf'\b{fieldName}\b', f'"{fieldName}"', query)
    
    # Remove any backslashes
    query = query.replace("\\", "")
    
    return query
    
    
# Actual query function
def Query(query):
    # Preprocess the query (adding quotation marks...)
    processedQuery = PreprocessQuery(query)
    
    print(processedQuery)
    
    # Create result object
    result = {
        "type": "queryResult",
        "query": processedQuery,
        "data": None
    }
    
    # With block will close connection and cursor when everything is done
    with psycopg.connect(
        dbname   = os.getenv("DATABASE_NAME"),
        user     = os.getenv("DATABASE_USER"),
        password = os.getenv("DATABASE_PASSWORD"),
        host     = os.getenv("DATABASE_HOST"),
        port     = os.getenv("DATABASE_PORT")
    ) as connection:
        with connection.cursor() as cursor:
            cursor.execute(processedQuery)

            # Get column names from cursor description
            columns = [desc[0] for desc in cursor.description]
            
            # Fetch all rows as a list of dictionaries
            data = [dict(zip(columns, row)) for row in cursor.fetchall()]
            
            result['data'] = data
             
    return result


# GRAPH RELATED____________________________________________________________
def Graph(graphType, graphName):
    print(graphType + graphName)