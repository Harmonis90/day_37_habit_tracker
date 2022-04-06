import requests
import config
import datetime
pixela_endpoint = "https://pixe.la/v1/users"

pixela_params = {
    "token": f"{config.TOKEN}",
    "username": f"{config.USER_NAME}",
    "agreeTermsOfService": "yes",
    "notMinor": "yes",

}
# pixela_create_user = requests.post(url=pixela_endpoint, json=pixela_params)

pixela_graph_endpoint = f"{pixela_endpoint}/{config.USER_NAME}/graphs"
graph_config_params = {
    "id": f"{config.GRAPH_ID}",
    "name": f"{config.GRAPH_NAME}",
    "unit": f"{config.GRAPH_UNIT}",
    "type": f"{config.GRAPH_TYPE}",
    "color": f"{config.GRAPH_COLOR}"
}
user_header = {
    "X-USER-TOKEN": f"{config.TOKEN}"
}
# pixela_graph_request = requests.post(url=pixela_graph_endpoint, json=graph_config_params, headers=user_header)

pixela_pixel_endpoint = f"{pixela_graph_endpoint}/{config.GRAPH_ID}"
TODAY = datetime.date.today().strftime("%Y%m%d")
# delta = datetime.timedelta()
# day_delta = (datetime.date.today() - delta).strftime("%Y%m%d")
effort_percentage = input("Be honest. What percentage grade should you get for today's coding effort?\nEffort: ")
# Percentage grade for today's coding work
PIXEL_QUANTITY = "100"
pixel_body = {
    "date": f"{TODAY}",
    "quantity": f"{PIXEL_QUANTITY}"
}
pixela_pixel_request = requests.post(url=pixela_pixel_endpoint, json=pixel_body, headers=user_header)
print(pixela_pixel_request.text)
# change_unit = requests.put(url=pixela_pixel_endpoint, json=graph_config_params, headers=user_header)
