import selenium
import requests

response = requests.get("http://www.baidu.com")

header = response.headers
status = response.status_code
body = response.text

print(header)
print(status)
print(body)

list_header_elements = list()
list_header_contents = list()
for i in header:
    list_header_elements.append(i)

print(list_header_elements)

for i in list_header_elements:
    list_header_contents.append(header[i])

print(list_header_contents)

response_again = requests.get("http://www.baidu.com")
content = str(response_again.content, "utf-8")
print(content)
print("-" * 200)
with open("./data.html", "w") as f:
    print("-----------100-----------")
    f.write(content)
f.close
