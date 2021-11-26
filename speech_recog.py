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


#设置麦克风
r = sr.Recognizer()
mic = sr.Microphone()
import os

def pause(audio_text):
    if '暂停' in audio_text or '关闭' in audio_text or '退下' in audio_text or '走吧' in audio_text or '滚吧' in audio_text or '闭嘴' in audio_text or 'shut down' in audio_text.lower() or 'shutdown' in audio_text.lower():
        pass
        text_to_voice('OK, darling! im shutdown!')
        return 1


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
            text_to_voice('hello, im online!')
            try:
                audio = audio_record()
                test_1 = r.recognize_google(audio, language='cmn-Hans-CN')  # 这样设置language可以支持中文
            except:
                pass
                text_to_voice('repeat again, please!')
            print('识别成功！我: ', test_1)
            if '打开浏览器' in test_1 or '打开百度' in test_1:
                os.system('start chrome https://www.baidu.com')
            elif '音乐' in test_1 or '播放' in test_1 :
                url = 'https://www.kugou.com/yy/html/search.html#searchType=song&searchKeyWord={}'.format(test_1.split('播放')[-1])
                open_url(url)
                print('一首 《月亮代表我的心》 送给你！')
            elif '你是傻狗' in test_1:
                print('狗子: 你才是傻狗！')
            elif '股票' in test_1:
                print('狗子: 行情大涨！')
            elif '跟我读' in test_1 or '跟我说' in test_1:
                results = translator(test_1)
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
                        pass
                        text_to_voice('repeat again, please!')
            elif '作文' in test_1 or '文章' in test_1:
                text_to_voice(
                    '''
                    　　The newly-coined word "online education" may by no means sound strange to most people. During the past several years, hundreds of online education colleges have sprung up around China.
                    　　Why could online education be so popular in such a short period of time? For one thing, If we want to catch up with the development and the great pace of modern society, we all should possess an urgent and strong desire to study, while most people nowadays are under so enormous pressures that they can hardly have time and energy to study full time at school. Furthermore, online education enables them to save a great deal of time on the way spent on the way between home and school. Last but not least, the quick development of internet，which makes possible all our dreams of attending class on the net，should also be another critical reason.
                    '''
                )



        else:
            print('狗子: 听不见！')


    except Exception as e:
        print('识别失败！狗子: 听不见！')
        print(e)
    print('')