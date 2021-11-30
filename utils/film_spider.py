# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File:           film_spider.py
   Description:
   Author:         Danny Wu
   Mail:           mrdanny1024@gmail.com 
   Create Date:    2021/11/29
-------------------------------------------------
   Modify:
                   2021/11/29:
-------------------------------------------------
"""
import requests
from lxml import etree

def get_imdb_code(film_name='沙丘'):
    # film_name = '沙丘'
    url = 'https://www.imdb.com/find?q={}&ref_=nv_sr_sm'.format(film_name)
    resp = requests.get(url)
    print(resp)
    html = etree.HTML(resp.text)
    try:
        film_imdb_code = html.xpath('//div[@id="content-2-wide"]/div[@id="main"]/div/div/table//td[@class="result_text"]/a/@href')[0].split('/')[2]
        print(film_imdb_code)
        return film_imdb_code
    except:
        pass
        return 'no result!'

def get_bt_link(imdb_code='tt1160419'):
    url = 'https://www.rarbgtorrents.org/torrents.php?category=4;14;48;17;44;45;47;50;51;52;42;46;54;18;41;49;23;25&search={}&order=seeders&by=DESC'.format(imdb_code)
    header = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
        'cookie': 'cf_clearance=sgXlQ7ffT5MP45.3UZvDQ7_XdvbBySbCIAbt15pNnvw-1636971903-0-150; __cf_bm=Rqo2i3qqr5lCdW..31fMeQ0btoCH4Fyp9wHWcQZmtnw-1638181417-0-AW8LuThwKC2OuEZWjDBt7rlDviUZhy1q+vaB2VLq3ckrXZJ0XJNRb2i6CZlnqust58Z7wolhgHrACyyVvXXhNNJA+TnmlspjxG+RQ3u7VDzGu56Mp6cMFQylKyQbycyRSA==; skt=6hu9si2vz9; gaDts48g=q8h5pp9t; skt=6hu9si2vz9; gaDts48g=q8h5pp9t; tcc; aby=2; ppu_main_9ef78edf998c4df1e1636c9a474d9f47=1; ppu_sub_9ef78edf998c4df1e1636c9a474d9f47=3',
        'dnt': '1',
        'referer': 'https://www.rarbgtorrents.org/torrents.php?category=4;14;48;17;44;45;47;50;51;52;42;46;54;18;41;49;23;25&search=tt1160419&order=seeders&by=ASC',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'
    }
    resp = requests.get(url, headers=header)
    print(resp.text)
    html = etree.HTML(resp.text)
    results = html.xpath('//table[@class="lista2t"]/tr[@class="lista2"]//@href')
    for i in results:
        # print(i.split('\n'))
        if '/torrent/' in i and '#comments' not in i:
            print('https://www.rarbgtorrents.org' + i)


if __name__ == '__main__':
    # get_imdb_code()
    get_bt_link()