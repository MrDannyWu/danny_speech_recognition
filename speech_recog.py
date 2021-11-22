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

import speech_recognition as sr
r = sr.Recognizer()                                              #调用识别器
test = sr.AudioFile(r"E:\Users\Danny\Desktop\t9hnz-qm5pv.wav")   #导入语音文件
with test as source:
    audio = r.record(source)
type(audio)
c=r.recognize_sphinx(audio, language='zh-cn')                    #识别输出
print(c)
