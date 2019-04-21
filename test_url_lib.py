# coding:utf-8
import requests
import json

# response = requests.get("http://www.baidu.com")
# print(type(response))
# print(response.status_code)
# print(response.text.encode("utf-8").decode("gbk"))
# print(response.content.decode("utf-8"))
# print(type(response.text))
# print(response.cookies)

# post_return = requests.post("http://httpbin.org/post")
# print(post_return.text)
# put_return = requests.put("http://httpbin.org/put")
# print(put_return.text)
# get_return = requests.get("http://httpbin.org/get")
# print(get_return.text)

# data = {
#     'name': 'Liu, Bei',
#     'age': 22
# }

# get_return_with_parameters = requests.get("http://httpbin.org/get", params=data)
# with open("./get_return_with_parameters.dat", "w") as f_get_return_with_parameters:
#     f_get_return_with_parameters.write(get_return_with_parameters.text)
# f_get_return_with_parameters.close()
#
# print("-----------json-------------------")
# print(get_return_with_parameters.json())
# with open("get_return_with_parameters.json","w") as f_get_return_with_parameters_json:
#     f_get_return_with_parameters_json.write(str(get_return_with_parameters.json()))
# print("--------json.load(get_return_with_parameters.text)----")
# print(json.loads(get_return_with_parameters.text))
# print(type(get_return_with_parameters.json()))

# 3.test headers
# request the web site without header is likely to be refused, like:
response = requests.get("http://www.zhihu.com")
print(response.text)

""" without header, you'll get:
<html>
<head><title>400 Bad Request</title></head>
<body bgcolor="white">
<center><h1>400 Bad Request</h1></center>
<hr><center>openresty</center>
</body>
</html>
"""
# test with header:
header = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
}

response_with_header = requests.get("http://www.zhihu.com", headers=header).content
print(response_with_header)
