import datetime
import requests
import base64
import json
from APP.data_models.rest_data_models.request_data_models import UploadPostData, LoginUser
from APP.utils.data_manger import save_file

# with open("logo_v3.png", "rb") as f:
#     data = f.read()
#
#
# data = base64.b64encode(data)
# data = data.decode('utf-8')
# file_name = "test"
# extension = "png"
# path = "C:\\Users\\blach\\PycharmProjects\\studentradeBackend\\"
#
# print(save_file(data, file_name, extension, path))




# content = "Lepiej"
# login = "a"
# password = "a"
#
#
# login_user = LoginUser(login=login, password=password)
# login_response = requests.post("http://192.168.0.106:8888/studentrade/v1/loginUser", data=login_user.json())
# login_response = json.loads(login_response.text)
# user_id = login_response['user_id']
# print(user_id)
# upload_post_data = UploadPostData(userId=user_id, content=content, image=data, fileName="test1",
#                                   extension="png")
# response = requests.put("http://192.168.0.106:8888/studentrade/v1/uploadPost", data=upload_post_data.json())
#
# print(response.text)
import os

print(os.getcwd())
