#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import multiprocessing
import time
import threading
import urllib2
import RPi.GPIO as GPIO

ID = 'pi' # <- チームのIDを入れる
URL = 'http://www.togawa.cs.waseda.ac.jp/~kotaro.terada/pi/data/' + ID + '.json'

PIN1 = 11
PIN2 = 13
PIN3 = 19
PIN4 = 21

GPIO.setmode(GPIO.BOARD)
# right
GPIO.setup(PIN1, GPIO.OUT)
GPIO.setup(PIN2, GPIO.OUT)
# left
GPIO.setup(PIN3, GPIO.OUT)
GPIO.setup(PIN4, GPIO.OUT)

Go=0
Back=0
Stop=0

# ここに取得データを元にして対象デバイスを動作させる処理を書く
def worker(input):

    # 取得値を表示
    print input['alpha'], input['beta'], input['gamma']

    # 以下てきとうな処理
    if input['beta'] < -30:
        GPIO.output(PIN2, False)
        GPIO.output(PIN1, False)
        GPIO.output(PIN4, False)
        GPIO.output(PIN3, True)
        print "Left"
    elif input['beta'] > 30:
        GPIO.output(PIN2,False)
        GPIO.output(PIN1,True)
        GPIO.output(PIN4,False)
        GPIO.output(PIN3,False)
        
        print "Right"
    else:
        if input ['gamma'] >30:     
            GPIO.output(PIN2, False)
            GPIO.output(PIN1, True)
            GPIO.output(PIN4, False)
            GPIO.output(PIN3, True)
            
            print "Go"
        elif input ['gamma'] <-30:     
            GPIO.output(PIN2, True)
            GPIO.output(PIN1, False)
            GPIO.output(PIN4, True)
            GPIO.output(PIN3, False)

            print"Back"
        else:     
            GPIO.output(PIN2, False)
            GPIO.output(PIN1, False)
            GPIO.output(PIN4, False)
            GPIO.output(PIN3, False)

            print"Stop"
    # 早過ぎたら適当にスリープする
    time.sleep(0.1)

# スマートフォンの傾きを研究室サーバから取得する処理
def fetch(data):
    data[0] = json.loads(urllib2.urlopen(URL).read())


# メインループ
if __name__ == '__main__':
    data = {}
    new_data = {}
    fetch(data)
    while True:
        # データ取得とデバイス操作は別スレッド
        # HTTP通信によるIO待ちをなるべく防ぐため
        th0 = threading.Thread(target=fetch, args=(new_data, ))
        th1 = threading.Thread(target=worker, args=(data[0], ))
        thlist = [th0, th1]
        th0.start()
        th1.start()
        for th in thlist:
            th.join()
        data = new_data
