# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File:           danny_translator.py
   Description:
   Author:
   Create Date:    2021/11/25
-------------------------------------------------
   Modify:
                   2021/11/25:
-------------------------------------------------
"""

import json
import requests
from text_to_voice import text_to_voice

# 语言列表
LAN_LIST = [
    'sq',
    'ar',
    'am',
    'az',
    'ga',
    'et',
    'or',
    'eu',
    'be',
    'bg',
    'is',
    'pl',
    'bs',
    'fa',
    'af',
    'tt',
    'da',
    'de',
    'ru',
    'fr',
    'tl',
    'fi',
    'fy',
    'km',
    'ka',
    'gu',
    'kk',
    'ht',
    'ko',
    'ha',
    'nl',
    'ky',
    'gl',
    'ca',
    'cs',
    'kn',
    'co',
    'hr',
    'ku',
    'la',
    'lv',
    'lo',
    'lt',
    'lb',
    'rw',
    'ro',
    'mg',
    'mt',
    'mr',
    'ml',
    'ms',
    'mk',
    'mi',
    'mn',
    'bn',
    'my',
    'hmn',
    'xh',
    'zu',
    'ne',
    'no',
    'pa',
    'pt',
    'ps',
    'ny',
    'ja',
    'sv',
    'sm',
    'sr',
    'st',
    'si',
    'eo',
    'sk',
    'sl',
    'sw',
    'gd',
    'ceb',
    'so',
    'tg',
    'te',
    'ta',
    'th',
    'tr',
    'tk',
    'cy',
    'ug',
    'ur',
    'uk',
    'uz',
    'es',
    'iw',
    'el',
    'haw',
    'sd',
    'hu',
    'sn',
    'hy',
    'ig',
    'it',
    'yi',
    'hi',
    'su',
    'id',
    'jw',
    'en',
    'yo',
    'vi',
    'zh-CN'
]

def translator(from_lan_content, from_lan='zh-CN', to_lan='en-US'):
    """

    :param from_lan_content:
    :param from_lan:
    :param to_lan:
    :return:
    """

    url = 'https://translate.googleapis.com/translate_a/single?'\
        'client=gtx&'\
        'sl=auto&'\
        'hl={}&' \
        'tl={}&' \
        'dt=t&'\
        'dt=bd&'\
        'dj=1&'\
        'tk=523672.523672&'\
        'q={}'.format(from_lan, to_lan, from_lan_content)

    resp = requests.get(url)
    # with open('a.json', 'wb') as f:
    #     f.write(resp.content)
    json_data = json.loads(resp.content.decode())
    # print(json_data)
    # print(len(json_data['sentences']))
    # print(json_data['sentences'])
    translation_result = ''
    for i in json_data['sentences']:
        # print(i)
        to_lan_content_row= i['trans']
        # print(to_lan_content_row)
        translation_result = translation_result + to_lan_content_row
    return translation_result


if __name__ == '__main__':
    from_lan_content = '''
    你好，我是中国人，中国人不骗中国人！
    '''
    # from_lan = 'en-US'
    from_lan = 'zh-CN'
    # to_lan = 'zh-CN'
    to_lan = 'en-US'
    translation_result = translator(from_lan_content, from_lan, to_lan)
    text_to_voice(translation_result)
    print(translation_result)