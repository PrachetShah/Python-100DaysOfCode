import requests
from datetime import datetime

pixela_endpoint = "https://pixe.la/v1/users"
TOKEN = "fuiw47yhhdhv"
USERNAME = "prachet25"
GRAPH_ID = "graph2"

# Creating a User
user_params = {
    # Add random token
    "token": TOKEN,
    "username": USERNAME ,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# # POST Takes json as parameters
# response = requests.post(url=pixela_endpoint,json=user_params)
# print(response.text)

# Creating a Graph
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Walking Graph",
    "unit" : "km",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

today = datetime.now()
today = today.strftime("%Y%m%d")

# Adding a Pixel
add_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
pixel_config = {
    # Read strftime documentation online to learn abt diff placeholders
    "date": today,
    "quantity": "9.5"
}

# response = requests.post(url=add_pixel_endpoint, json=pixel_config, headers=headers)
# print(response.text)

# PUT changes the data and DELETE deleted the data

# Changing Values using PUT
change_value_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today}"
change_param = {
    "quantity": "10"
}
# response = requests.put(url=change_value_endpoint, json=change_param, headers=headers)
# print(response.text)

# Deleting a Pixel
delete_endpoint = change_value_endpoint
# No delete params req
# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)
