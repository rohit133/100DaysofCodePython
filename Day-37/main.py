import requests
from datetime import datetime

USER_LOG = "https://pixe.la/v1/users/rohit0day/graphs/graph1.html"

USERNAME= "rohit0day"
TOKEN = "drit42uthu8934tu"
ID = "graph1"
DATE = datetime(year=2022,month=1,day=10).strftime("%Y%m%d")

headers = {
    "X-USER-TOKEN": TOKEN
}

user_params= {
    "token":TOKEN,
    "username":USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes",
}


graph_config = {
    "id":ID,
    "name":"Coding",
    "unit":"commit",
    "type":"float",
    "color":"ajisai"
}


posting_params = {
    "date":DATE,
    "quantity":"17",
}


updating_post_params = {
    "quantity":"7",
}

pixela_endpoint = "https://pixe.la/v1/users"
# response = requests.post(url=pixela_endpoint,json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
# response = requests.post(url=graph_endpoint,json=graph_config,headers=headers)
# print(response.text)

posting_pixela_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{ID}"
# response = requests.post(url=posting_pixela_endpoint,json=posting_params,headers=headers)
# print(response.text)

posting_pixela_Updates_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{ID}/{DATE}"
# response = requests.put(url=posting_pixela_Updates_endpoint,json=updating_post_params,headers=headers)
# print(response.text)

deleting_post_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{ID}/{DATE}"
response = requests.delete(url=deleting_post_endpoint,headers=headers)
print(response.text)
