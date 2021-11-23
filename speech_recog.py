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
#设置麦克风
r = sr.Recognizer()
mic = sr.Microphone()
import os

def audio_record():
    print('狗子: 录音中...')
    with mic as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    # 进行识别
    print('狗子: 录音结束，识别中...')
    return audio

#进行录音
while True:
    try:
        audio = audio_record()
        # test = r.recognize_sphinx(audio, language='zh-cn')#这样设置language可以支持中文
        test = r.recognize_google(audio, language='cmn-Hans-CN')#这样设置language可以支持中文
        print('识别成功！我: ', test)  # 最后将识别的文字打印出来
        if '狗子' in test:
            print('狗子: 收到！请说:')
            audio = audio_record()
            test_1 = r.recognize_google(audio, language='cmn-Hans-CN')  # 这样设置language可以支持中文
            print('识别成功！我: ', test_1)
            if '打开浏览器' in test_1:
                os.system('start chrome')
            elif '音乐' in test_1:
                os.system('start chrome https://music.163.com/#/song?id=229223')
                print('一首 《月亮代表我的心》 送给你！')
            elif '你是傻狗' in test_1:
                print('狗子: 你才是傻狗！')
            elif '股票' in test_1:
                print('狗子: 行情大涨！')
        else:
            print('狗子: 听不见！')


    except:
        print('识别失败！狗子: 听不见！')
    print('')