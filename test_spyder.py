import selenium
import requests

response = requests.get("http://www.baidu.com").text.encode("utf-8").decode("gbk")
response_again = requests.get("http://www.baidu.com").content.decode("utf-8")
print("-" * 200)
with open("./data.dat", "w") as f:
    print("-----------100-----------")
    f.write(response_again)
f.close
with open("./dat_utf_8.html", "w") as f1:
    f1.write(response)
f1.close()
print("--->f1 written<---")
