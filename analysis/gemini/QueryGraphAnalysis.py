import os
from dotenv import load_dotenv
import re
import psycopg
import decimal
import datetime
import matplotlib.pyplot as plt
import io
import base64
import numpy as np
from sklearn.linear_model import LinearRegression

# GRID THRESHOLD
threshold = 50

# Import gemini function
from analysis.gemini.Functions.GenerateResponse import *

load_dotenv()

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
    
    # TEST
    print("The query after processing is")
    print(processedQuery)
    
    # Create result object
    result = {
        "type": "queryResult",
        "query": processedQuery,
        "content": None
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
            data = []
            for row in cursor.fetchall():
                # Create dictionary for each row and convert decimals and datetimes
                row_dict = {
                    col: (
                        float(value) if isinstance(value, decimal.Decimal) else
                        value.isoformat() if isinstance(value, datetime.datetime) else
                        value
                    )
                    for col, value in zip(columns, row)
                }
                data.append(row_dict)
            
            result['content'] = data

             
    # TEST
    print(result)
             
    return result


# GRAPH RELATED____________________________________________________________
def Graph(graphType, data, result):
    # Preprocess graphtype
    graphType = graphType.replace("\n", "")
    # print("This graph is a " + graphType + " graph")
    
    # Draw the graph
    if graphType == 'line':
        # Extract x-axis label (first key)
        x_axis_label = list(data[0].keys())[0]
        x_axis = [entry[x_axis_label] for entry in data]

        # Extract y-axis data for each remaining key
        y_axes = {key: [entry[key] for entry in data] for key in data[0] if key != x_axis_label}

        # Plot each y-axis on a separate plot
        for label, y_axis in y_axes.items():
            plt.figure(figsize=(10, 6))
            plt.plot(x_axis, y_axis, marker='o', linestyle='-', linewidth=2, markersize=6, label=label)

            # Add labels and title
            plt.xlabel(x_axis_label)
            plt.ylabel(label)
            plt.title(f'{label} over {x_axis_label}')
            plt.legend()  # Show legend for the y-axis label
            
            # Conditionally add grid based on the number of points
            if len(y_axis) <= threshold:
                plt.grid(True)
            else:
                plt.grid(False)

            # Show each plot
            # plt.show()
            
            # Create data for this particular window
            temporaryData = []
            for (x, y) in zip(x_axis, y_axis):
                item = {
                    x_axis_label: x,
                    label: y
                }
                temporaryData.append(item)
        
            # Convert the plot to hase64
            buffer = io.BytesIO()
            plt.savefig(buffer, format='png')
            buffer.seek(0)
            img_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
            
            # Generate an overview for the graph
            overview = GenerateGraphOverview(temporaryData, buffer)
            
            # Close the buffer 
            buffer.close()
            
            # Create result template
            item = {
                "type": "graphResult",
                # "graphType": graphType,
                "content": img_base64,
            }
            
            # Add temporary result to list
            result['list'].append(item)
            
            # Add overview text to list
            overviewItem = {
                "type": "text",
                "content": overview
            }
            result['list'].append(overviewItem)
        
    elif graphType == 'bar':
        # Extract the category label (first key) and category values
        category_label = list(data[0].keys())[0]
        categories = [entry[category_label] for entry in data]

        # Extract y-axis data for each remaining key
        y_axes = {key: [entry[key] for entry in data] for key in data[0] if key != category_label}

        # Plot each y-axis on separate bar graphs
        for label, values in y_axes.items():
            plt.figure(figsize=(8, 6))
            plt.bar(categories, values, color='skyblue')
            plt.xlabel(category_label)
            plt.ylabel(label)
            plt.title(f'Bar Graph of {label}')
            
            #plt.show()
            
            # Create data for this particular window
            temporaryData = []
            for (x, y) in zip(categories, values):
                item = {
                    category_label: x,
                    label: y
                }
                temporaryData.append(item)
        
            # Convert the plot to hase64
            buffer = io.BytesIO()
            plt.savefig(buffer, format='png')
            buffer.seek(0)
            img_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
            
            # Generate an overview for the graph
            overview = GenerateGraphOverview(temporaryData, buffer)
            
            # Close the buffer 
            buffer.close()
            
            # Create result template
            item = {
                "type": "graphResult",
                # "graphType": graphType,
                "content": img_base64,
            }

            # Add temporary result to list
            result['list'].append(item)
            
            # Add overview text to list
            overviewItem = {
                "type": "text",
                "content": overview
            }
            result['list'].append(overviewItem)
    
    elif graphType == 'pie':
        print("draw a pie")
        
    elif graphType == 'predict':
        # Separate the data based on 'original' attribute
        original_values = [item["value"] for item in data if item["original"]]
        predicted_values = [item["value"] for item in data if not item["original"]]
        original_indices = list(range(len(original_values)))
        predicted_indices = list(range(len(original_values), len(original_values) + len(predicted_values)))

        # Plotting
        plt.figure(figsize=(10, 6))
        plt.plot(original_indices, original_values, color="blue", label="Original Data", marker="o")
        plt.plot(predicted_indices, predicted_values, color="orange", label="Predicted Data", marker="o")

        # Connect the last original data point to the first predicted data point with the same color as the predicted line
        plt.plot([original_indices[-1], predicted_indices[0]], [original_values[-1], predicted_values[0]], color="orange", linestyle="--")

        plt.xlabel("Index")
        plt.ylabel("Value")
        plt.title("Original vs Predicted Data (Connected)")
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        
        # plt.show()
    
        # Create data for this particular window
        # temporaryData = []
        # for (x, y) in zip(x_axis, y_axis):
        #     item = {
        #         x_axis_label: x,
        #         label: y
        #     }
        #     temporaryData.append(item)
    
        # Convert the plot to hase64
        buffer = io.BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        img_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
        
        # Generate an overview for the graph
        # overview = GenerateGraphOverview(temporaryData, buffer)
        
        # Close the buffer 
        buffer.close()
        
        # Create result template
        item = {
            "type": "graphResult",
            # "graphType": graphType,
            "content": img_base64,
        }

        # Add temporary result to list
        result['list'].append(item)

def Predict(data, step):
    # Extract 
    y_axis_label = list(data[0].keys())[-1]
    y_axis = [entry[y_axis_label] for entry in data]
    
    # Step 2: Prepare data for training
    x = np.arange(len(y_axis)).reshape(-1, 1)  # Positions as x (0, 1, 2, ...)
    y = np.array(y_axis)  # Values as y

    # Step 3: Train linear regression model
    model = LinearRegression()
    model.fit(x, y)

    # Step 4: Predict future steps
    future_steps = np.array([len(y_axis) + i for i in range(1, step + 1)]).reshape(-1, 1)  # Next 3 steps
    predictions = model.predict(future_steps)

    # Create data for graphing
    graphData = []
    for item in y_axis:
        template = {
            "original": True,
            "value": item
        }
        graphData.append(template)
    
    for item in predictions:
        template = {
            "original": False,
            "value": float(item)
        }
        graphData.append(template)
        
    print(graphData)
    return graphData