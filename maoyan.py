import requests
import re
from requests.exceptions import RequestException
import json
from multiprocessing import Pool


def get_one_page(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        else:
            return None
    except RequestException:
        return None


def parse_one_page(html):
    pattern = re.compile(
        "<dd>.*?board-index.*?>(\d+)</i>.*?data-src=\"(.*?)\".*?<a href=.*?title=\"(.*?)\".*?<p class=\"star\">(.*?)</p>.*?<p class=\"releasetime\">(.*?)</p>.*?</dd>",
        re.S)

    result = re.findall(pattern, html)
    for item in result:
        yield {
            'index': item[0],
            'image': item[1],
            'title': item[2],
            'actor': item[3].strip()[3:],
            'year': item[4].strip()[5:]
        }


def write_to_file(content):
    with open("./猫眼电影排名信息.txt", "a", encoding="utf-8") as f:
        f.write(json.dumps(content, ensure_ascii=False) + '\n')
    f.close()


def main(offset):
    url = "http://maoyan.com/board/4?offset=" + str(offset)
    html = get_one_page(url)
    print(html)

    print('-' * 250)
    for item in parse_one_page(html):
        print(item)
        write_to_file(item)


if __name__ == "__main__":
    for i in range(10 ):
        main(i*10)
    # print("before_main()")
    # pool = Pool()
    # pool.map(main, [i*10 for i in range(10)])
