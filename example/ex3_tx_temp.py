#!/usr/bin/env python3
# coding: utf-8

# TCPを送信する
# Copyright (c) 2021-2025 Wataru KUNINO

# TCPで温度値を送信します。(外付けセンサ不要)
# ./ex3_tx_temp.py

import socket                                               # ソケットの組み込み
from time import sleep                                      # スリープの組み込み
from lib_tempSensor import TempSensor                       # 温度センサ組み込み

port = 8080                                                 # ポート番号を代入
tempSensor = TempSensor()                                   # 温度センサの実体化
tempSensor.offset = 30                                      # 補正値30を設定

while True:                                                 # 繰り返し構文
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM) # TCP用ソケット作成
    sock.connect(('127.0.0.1', port))                       # TCP接続
    temp = round(tempSensor.get(), 1)                       # 温度値を取得
    tcp = 'temp._1,' + str(temp) + '\n'                     # 送信文字列を生成
    sock.sendall(tcp.encode())                              # メッセージ送信
    print('send :', tcp, end='')                            # 送信データを出力
    sock.close()                                            # 切断
    sleep(10)                                               # 10秒の待ち時間処理

'''
pi@raspberrypi:~/tcp/learning $ ./ex3_tx_temp.py
send : temp._1,25.5
send : temp._1,26.5
send : temp._1,25.5
send : temp._1,24.5
'''
