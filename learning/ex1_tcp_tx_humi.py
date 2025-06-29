#!/usr/bin/env python3
# coding: utf-8

# TCPクライアント：TCPで温度値と湿度値を送信します。(外付けセンサ = SHT30)
# Copyright (c) 2021-2025 Wataru KUNINO

import socket                                               # ソケットの組み込み
from time import sleep                                      # スリープの組み込み
from lib_humiSensorSHT4 import HumiSensor                   # センサ組み込み

port = 8080                                                 # ポート番号を代入
humiSensor = HumiSensor()                                   # センサの実体化

while True:                                                 # 繰り返し構文
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM) # TCP用ソケット作成
    sock.connect(('127.0.0.1', port))                       # TCP接続
    (temp, humi) = humiSensor.get()                         # 温度と湿度値を取得
    tcp = 'humid_1,' + str(round(temp, 1)) + ', '           # 送信文字列を生成
    tcp += str(round(humi, 2)) + '\n'                       # 湿度値を追加
    sock.sendall(tcp.encode())                              # メッセージ送信
    print('send :', tcp, end='')                            # 送信データを出力
    sock.close()                                            # 切断
    sleep(10)                                               # 10秒の待ち時間処理

'''
send : humid_1,29.7, 56.13
send : humid_1,29.7, 56.18
send : humid_1,29.7, 56.18
send : humid_1,29.7, 56.14
send : humid_1,29.7, 56.14
'''
