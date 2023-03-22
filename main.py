import requests
import datetime

PIXELA_END_POINT = "https://pixe.la/v1/users"
TOKEN = "alfiolandar"
USER_NAME = "mbernaboar"
now = datetime.datetime.now()
TODAY = now.strftime("%Y%m%d")
GRAPH_ID = "graph1"
PIXELA_HEADER = {
    "X-USER-TOKEN": TOKEN
}
# user_params = {
#     "token": "alfiolandar",
#     "username": "mbernaboar",
#     "agreeTermsOfService": "yes",
#     "notMinor": "yes",
# }
# response = requests.post(url=PIXELA_END_POINT, json=user_params)
# print(response.text)

# GRAPH_END_POINT = f"{PIXELA_END_POINT}/{USER_NAME}/graphs"
#
#
# graph_params = {
#     "id": GRAPH_ID,
#     "name": "Horas dedicadas al curso",
#     "unit": "hours",
#     "type": "int",
#     "color": "sora",
# }

# response = requests.post(url=GRAPH_END_POINT, headers=GRAPH_HEADER, json=graph_params)
# print(response.text)

POST_END_POINT = f"{PIXELA_END_POINT}/{USER_NAME}/graphs/{GRAPH_ID}"

graph_update_params = {
    "date": TODAY,
    "quantity": input("Cuántas horas codeaste hoy? ")
}
response = requests.post(url=POST_END_POINT, headers=PIXELA_HEADER, json=graph_update_params)
print(response.text)

# PUT_END_POINT = f"{PIXELA_END_POINT}/{USER_NAME}/graphs/{GRAPH_ID}/{TODAY}"
#
# put_json = {
#     "quantity": "3"
# }
#
# response = requests.put(url=PUT_END_POINT, headers=PIXELA_HEADER, json=put_json)
# print(response.text)

# DELETE_END_POINT = f"{PIXELA_END_POINT}/{USER_NAME}/graphs/{GRAPH_ID}/{TODAY}"
#
# response = requests.delete(url=DELETE_END_POINT, headers=PIXELA_HEADER)
# print(response.text)