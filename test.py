#
from APP.utils.data_manger import generate_title_filter

# test_data = {
#     'image': 'D:\PyCharm\StudentTrade\storage\logo_v3.png.png'
# }
#
# data = [test_data]
# # with open(test_data['image'], 'rb') as f:
# #     print(f.read())
# print(get_posts_image(data))


data = generate_title_filter(title="Programowanie obiektowe bla bla bla")
print(data)


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
