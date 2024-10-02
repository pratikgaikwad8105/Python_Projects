import requests
import datetime


pexela_endpoint = "https://pixe.la/v1/users"

USERNAME = "gaikwadpratik8105"
TOKEN = "Pratik@8105"

user_parameters = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pexela_endpoint, json=user_parameters)
# print(response.text)

graph_endpoint = f"{pexela_endpoint}/{USERNAME}/graphs"

graph_parameters = {
    "id": "graph1",
    "name": "Exercise Graph",
    "unit": "min",
    "type": "int",
    "color": "momiji"
}

header = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_parameters, headers=header)
# print(response.text)

data_endpoint = f"{graph_endpoint}/graph1"

today = datetime.datetime.now()

yesterday = today - datetime.timedelta(days=1)

date = today.strftime("%Y%m%d")

input_data_parameters = {
    "date": date,
    "quantity": "60",
}

# response = requests.post(url=data_endpoint, json=input_data_parameters, headers=header)
# print(response.text)

data_update_endpoint = f"{data_endpoint}/{yesterday.strftime("%Y%m%d")}"

update_parameters = {
    "quantity": "30"
}

# response = requests.put(url=data_update_endpoint, json=update_parameters, headers=header)
# print(response.text)

response = requests.delete(url=data_update_endpoint, headers=header)
print(response.text)