#!/usr/bin/env python
# -*- coding: utf-8 -*-
########################################################################
# 
# Copyright (c) 2017 aibot.me, Inc. All Rights Reserved
# 
########################################################################


"""PyAudio Example: Play a WAVE file."""

import pyaudio
import wave
import os
import time


input_filename = "name.wav"               # 麦克风采集的语音输入
            # 输入文件的path
in_path = input_filename

def get_audio(filepath):
    # aa = str(input("是否开始录音？   （是/否）"))
    # if aa == str("是") :
        CHUNK = 256
        FORMAT = pyaudio.paInt16
        CHANNELS = 1                # 声道数
        RATE = 16000               # 采样率
        RECORD_SECONDS =5
        WAVE_OUTPUT_FILENAME = filepath
        p = pyaudio.PyAudio()

        stream = p.open(format=FORMAT,
                        channels=CHANNELS,
                        rate=RATE,
                        input=True,
                        frames_per_buffer=CHUNK)
        print("*"*10, "开始录音：请在{}秒内输入语音".format(RECORD_SECONDS))
        frames = []
        for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
            data = stream.read(CHUNK)
            frames.append(data)
        print("*"*10, "录音结束\n")

        stream.stop_stream()
        stream.close()
        p.terminate()

        wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))
        wf.close()


get_audio(in_path )