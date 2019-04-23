# encoding: utf-8
import re
import requests

# string = "Hello 1234567 World_This is a \r\nRegex Demo"
#
# result = re.match('^Hello\s\d\d\d\s\d+\s', string)
# dict_res = dict()
#
# result = re.match("Hello(.*)\r\n.*Demo", string)
# print(result.group(1))

douban_html = requests.get("http://book.douban.com")
with open("./douban_html.html", "w+") as f:
    f.write(douban_html.text)
f.close()
