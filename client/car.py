#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import multiprocessing
import time
import threading
import urllib2

ID = 'test' # <- チームのIDを入れる
URL = 'http://www.togawa.cs.waseda.ac.jp/~kotaro.terada/pi/data/' + ID + '.json'


# ここに取得データを元にして対象デバイスを動作させる処理を書く
def worker(input):

    # 取得値を表示
    print input['alpha'], input['beta'], input['gamma']

    # 以下てきとうな処理
    if input['alpha'] < 0:
        right_tire = True
        left_tire = False
    elif input['alpha'] > 0:
        right_tire = False
        left_tire = True
    else:
        right_tire = False
        left_tire = False

    # 早過ぎたら適当にスリープする
    time.sleep(0.5)


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
