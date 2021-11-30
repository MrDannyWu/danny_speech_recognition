# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File:           weather.py
   Description:
   Author:         Danny Wu
   Mail:           mrdanny1024@gmail.com 
   Create Date:    2021/11/30
-------------------------------------------------
   Modify:
                   2021/11/30:
-------------------------------------------------
"""
import requests
from lxml import etree
url = 'https://2021.ip138.com/'

header = {
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'DNT': '1',
    'Host': '2021.ip138.com',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'
}
resp = requests.get(url, headers=header)
print(resp)
address = resp.text.split(' 来自：')[-1].split('</p>')[0].strip().split(' ')[0]
print(address)

weather_url = 'http://www.baidu.com/s?wd={}天气'.format(address)
resp_weather = requests.get(weather_url)
resp_weather.encoding = 'utf-8'
print(resp_weather.text)
html = etree.HTML(resp_weather.text)
results = html.xpath('//div[@id="content_left"]/div[@id="1"]/@mu')
print(results)
