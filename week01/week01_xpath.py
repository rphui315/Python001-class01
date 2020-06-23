import requests
from lxml import etree

url = "https://maoyan.com/films?showType=3"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 OPR/26.0.1656.60"
}

response = requests.get(url=url, headers=headers)
response.encoding = "utf-8"

html = etree.HTML(response.text)
dd_list = html.xpath("//dl[@class='movie-list']//dd")
print(dd_list)


