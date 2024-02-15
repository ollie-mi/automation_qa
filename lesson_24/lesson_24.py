import requests
import lxml.html
from lxml.html import fromstring, fragment_fromstring
from lxml import etree
from io import StringIO


def get_page(url):
    r = requests.get(url)
    return r.content

def get_xpath(content, x_path):
    tree = fromstring(content)
    text = tree.xpath(x_path)
    return text

broken_html = """<html><head>
<title>test<body><h1>page title</h3>
<a rel='my@mail.com'>click me</a>
<p class='abc' > some text
<div id="xyz"> text </div>
""" # неевірний покоцаний хтмл


if __name__ == "__main__":
    url = "https://lxml.de/index.html"
    xpath = '//*[@id="introduction"]//text()'
    html = get_page(url)
    text_part = get_xpath(html, xpath)
    # print(text_part)
    parser = etree.HTMLParser()
    tree = etree.parse(StringIO(broken_html), parser)  # перетворюєм в зрозумілу структуру
    result = etree.tostring(tree.getroot(),
                pretty_print=True, method="html")  # звороне перетворення - обєкт дерева у строку
    print(result.decode("utf-8"))
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(str(result.decode("utf-8")))
