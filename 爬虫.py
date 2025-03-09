import requests
import re


url='https://www.weather.com.cn/weather/101271409.shtml'
resp=requests.get(url)
resp.encoding='utf-8'
print(resp.text)
date=re.findall('<a href="/weather1d/101271409.shtml">([\u4e00-\u9fa5])</a>',resp.text)
print((date))