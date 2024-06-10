import requests
import json
from main import get_gpt4_json_response

# SharePoint site and list details
site_url = "https://yoursharepointsite.com/sites/yoursite"
list_name = "YourListName"
url = f"{site_url}/_api/web/lists/getbytitle('{list_name}')/items"

# Authentication details
username = "your_username"
password = "your_password"

# Headers for the POST request
headers = {
    "Accept": "application/json;odata=verbose",
    "Content-Type": "application/json;odata=verbose"
}

# Function to add items to the SharePoint list
def add_items_to_sharepoint(data):
    for item in data:
        response = requests.post(url, json=item, headers=headers, auth=(username, password))
        if response.status_code == 201:
            print("Item added successfully")
        else:
            print(f"Failed to add item: {response.content}")

# Prompt for GPT-4
prompt = "Generate a JSON object with the data needed for the SharePoint list."

# Get JSON data from GPT-4
json_response = get_gpt4_json_response(prompt)

# Convert JSON string to Python object
data = json.loads(json_response)

# Add items to SharePoint list
add_items_to_sharepoint(data)