from bs4 import BeautifulSoup
import lxml

with open('./test_douban_books.html', 'r') as f:
    html = f.read()
soup = BeautifulSoup(html, 'lxml')
print(soup.prettify())
print("-" * 250)
print(soup.title.string)
print("-" * 250)
print(soup.head)
print("-" * 250)
print(soup.p)
print("-" * 250)
print(soup.title.name)

