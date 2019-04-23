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
# response = requests.get("http://www.zhihu.com")
# print(response.text)
#
# """ without header, you'll get:
# <html>
# <head><title>400 Bad Request</title></head>
# <body bgcolor="white">
# <center><h1>400 Bad Request</h1></center>
# <hr><center>openresty</center>
# </body>
# </html>
# """
# # test with header:
# header = {
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
# }
#
# response_with_header = requests.get("http://www.zhihu.com", headers=header)
# with open("./zhihu.html", "w", encoding="utf-8") as f_zhihu_html:
#     f_zhihu_html.write(response_with_header.text)
#
# print(response_with_header)

# 下载一张图片：
# response = requests.get("https://www.baidu.com/img/xinshouye_c9d9de2ff40fa160f807f75f34db4ad0.gif")
# with open(".\google_icon.gif", "wb") as google_icon:
#     google_icon.write(response.content)
# google_icon.close()
# 上传图片：
# with open(".\google_icon.gif", "rb") as google_icon_:
#     files = {'file': google_icon_}
#     response = requests.post("http://httpbin.org/post", files=files)
# print("----->" + response.text)

# -------------------------------------------------------------------------------------------
# 获取cookie:
# header = {
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
# }
# response_get_cookie = requests.get("http://www.baidu.com", headers=header)
# print(response_get_cookie.cookies)
# print("-" * 200)
# for key, value in response_get_cookie.cookies.items():
#     print(key + "<--->" + value)

# requests.get("http://httpbin.org/cookies/set/number/987654321")
# response_set_and_get_cookies = requests.get("http://httpbin.org/cookies")
# print(response_set_and_get_cookies.text)

# # 保持对话： Session()类：
# session_instance = requests.Session()
# session_instance.get("http://httpbin.org/cookies/set/number/987654321")
# response = session_instance.get("http://httpbin.org/cookies")
# print(response.text)

# # 证书验证：
# response_verify = requests.get("http://www.12306.com")
# print("--------------")
# print(response_verify.status_code)
# print("--------------")

# # 设置代理：
# proxies = {
#     "http": "http://:9743",
#     "https": "https://127.0.0.1:9743",
# }
# response_proxy = requests.get("https://www.taobao.com", proxies=proxies)
# print(response_proxy)


