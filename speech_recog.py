# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File:           speech_recog.py
   Description:
   Author:        
   Create Date:    2021/11/22
-------------------------------------------------
   Modify:
                   2021/11/22:
-------------------------------------------------
"""

# 引入
from threading import Thread
import speech_recognition as sr
from browser_app import open_url
from threading import Thread
from text_to_voice import text_to_voice
from danny_translator import translator
import random

#设置麦克风

import os

r = sr.Recognizer()
mic = sr.Microphone()


def pause(audio_text):
    """
    让狗子关闭
    :param audio_text:
    :return:
    """
    if '暂停' in audio_text or '关闭' in audio_text or '退下' in audio_text or '走吧' in audio_text or '滚吧' in audio_text or '闭嘴' in audio_text or 'shut down' in audio_text.lower() or 'shutdown' in audio_text.lower():
        # text_to_voice('OK, darling! im shutdown!')
        text_to_voice('好的主人，我这就退下！')
        return 1
    else:
        return False


def audio_record():
    """
    录音
    :return:
    """
    print('狗子: 录音中...')
    with mic as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    # 进行识别
    print('狗子: 录音结束，识别中...')
    return audio


def tips():
    """
    Missed
    提示用户如何与狗子沟通,或者用户的语音未命中，来时用户的语音输入
    :return:
    """
    # print('请尝试说:今天天气怎么样！')
    # print('刚刚开小车去了，没听见，请再说一次！')
    text_to_voice('刚刚开小车去了，没听见，请再说一次！')


def read_with_me(audio_text):
    """
    跟我读功能
    :param audio_text:
    :return:
    """
    results = translator(audio_text)
    text_to_voice(results)
    while True:
        try:
            follow_audio = audio_record()
            follow_audio_results = r.recognize_google(follow_audio, language='cmn-Hans-CN')
            results_1 = translator(follow_audio_results)
            text_to_voice(results_1)
            if pause(follow_audio_results):
                break
        except:
            # text_to_voice('repeat again, please!')
            tips()


def open_browser(audio_text):
    """
    打开浏览器
    :param audio_text:
    :return:
    """
    os.system('start chrome https://www.baidu.com')


def stock_info():
    """
    股市播报
    :return:
    """
    print('狗子: 行情大涨！')


def read_article_aloud():
    """
    朗读文章
    :return:
    """
    text_to_voice(
        '''
        　　The newly-coined word "online education" may by no means sound strange to most people. During the past several years, hundreds of online education colleges have sprung up around China.
        　　Why could online education be so popular in such a short period of time? For one thing, If we want to catch up with the development and the great pace of modern society, we all should possess an urgent and strong desire to study, while most people nowadays are under so enormous pressures that they can hardly have time and energy to study full time at school. Furthermore, online education enables them to save a great deal of time on the way spent on the way between home and school. Last but not least, the quick development of internet，which makes possible all our dreams of attending class on the net，should also be another critical reason.
        '''
    )


def play_music(audio_msg_text):
    """
    根据语音文本内容播放音乐
    语音最好为播放xxx(歌名)，若没有提到歌名，将启动推荐系统
    :param audio_msg_text:
    :return:
    """
    music_name = audio_msg_text.split('播放')[-1]
    url = 'https://www.kugou.com/yy/html/search.html#searchType=song&searchKeyWord={}'.format(music_name)
    open_url(url)
    print('一首 《月亮代表我的心》 送给你！')


def stupid_dog():
    """
    当用户语音在包含傻狗时，狗子的回应
    :return:
    """
    print('狗子: 你才是傻狗！')


def weather_broadcast():
    """
    天气播报
    :return:
    """
    text_to_voice('天气好极了！')
    pass


def wake_up_to_answer():
    """
    唤醒回答
    :return:
    """
    # text_to_voice('hello, im online!')
    answer = []
    text_to_voice('你好，主人，我在呢', rate=150)


def recognize_failure():
    """
    识别失败提示
    :return:
    """
    text_to_voice('没听清，请再说一遍呢！')


def second_audio_text():
    """
    唤醒狗子后，用户说的第一句话
    :return:
    """
    try:
        audio = audio_record()
        audio_msg_text = r.recognize_google(audio, language='cmn-Hans-CN')  # 这样设置language可以支持中文
        return audio_msg_text
    except:
        recognize_failure()


def ai_dog():
    try:
        wake_up_audio = audio_record()
        # test = r.recognize_sphinx(audio, language='zh-cn')#这样设置language可以支持中文
        wake_up_audio_text = r.recognize_google(wake_up_audio, language='cmn-Hans-CN')  # 这样设置language可以支持中文
        print('识别成功！我: ', wake_up_audio_text)  # 最后将识别的文字打印出来
        if '狗子' in wake_up_audio_text:
            print('狗子: 收到！请说:')

            wake_up_to_answer()

            audio_msg_text = second_audio_text()

            print('识别成功！我: ', audio_msg_text)
            if '打开浏览器' in audio_msg_text or '打开百度' in audio_msg_text:
                open_browser(audio_msg_text)
            elif '音乐' in audio_msg_text or '播放' in audio_msg_text:
                play_music(audio_msg_text)
            elif '傻狗' in audio_msg_text:
                stupid_dog()
            elif '股票' in audio_msg_text:
                stock_info()
            elif '跟我读' in audio_msg_text or '跟我说' in audio_msg_text:
                read_with_me(audio_msg_text)
            elif '作文' in audio_msg_text or '文章' in audio_msg_text:
                read_article_aloud()
            elif '天气' in audio_msg_text:
                weather_broadcast()
        else:
            print('狗子: 听不见！')
            tips()

    except Exception as e:
        # print('识别失败！狗子: 听不见！')
        recognize_failure()
        print(e)

    print('')


def run():
    while True:
        ai_dog()


if __name__ == '__main__':
    run()
    # pause('关闭！')
