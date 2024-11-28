import requests
import json
from bs4 import BeautifulSoup

_url = 'https://www.bilibili.com/'
s = requests.get(_url)
s.encoding='utf-8'
print(s.text)
