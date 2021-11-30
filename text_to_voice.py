# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File:           text_to_voice.py
   Description:
   Author:
   Create Date:    2021/11/25
-------------------------------------------------
   Modify:
                   2021/11/25:
-------------------------------------------------
"""

import pyttsx3

def text_to_voice(text_content='Hello World!', rate=128, volume=1):
    engine = pyttsx3.init() # object creation

    """ RATE"""
    # rate = engine.getProperty('rate')   # getting details of current speaking rate
    # print (rate)                        #printing current voice rate
    engine.setProperty('rate', rate)     # setting up new voice rate

    engine.setProperty('voice', 'zh')
    """VOLUME"""
    # volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
    # print (volume)                          #printing current volume level
    engine.setProperty('volume', volume)    # setting up volume level  between 0 and 1

    """VOICE"""
    # voices = engine.getProperty('voices')       #getting details of current voice
    #engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
    # engine.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female
    # engine.say("我是中国人")
    # engine.say("Hello World!")
    engine.say(text_content)
    # engine.say('My current speaking rate is ' + str(rate))
    engine.runAndWait()
    engine.stop()

    """Saving Voice to a file"""
    # On linux make sure that 'espeak' and 'ffmpeg' are installed
    # engine.save_to_file('Hello World', 'test.mp3')
    # engine.runAndWait()

if __name__ == '__main__':
    text_to_voice('Hello everyone!')