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

# douban_html = requests.get("http://book.douban.com")
# with open(".\\test_douban_books.html", "w", encoding="utf-8") as f1:
#     f1.write(douban_html.text)
# f1.close()
with open("./test_douban_books.html","r") as f_read:
    str_page = f_read.read()
f_read.close()

# print(str_page)
print("-" * 250)

book_list = re.findall("<a class=.*?title=\"(.*?)\".*?</a>.*?<div class=\"author\">(.*?)>*?</div>", str_page, re.S)
print(book_list)
print("-" * 250)
for book in book_list:
    name, author = book
    author_strip = re.sub('\s', '', author)
    print(name, author_strip)


