#!/usr/bin/env python3
# coding: utf-8

# センサ用UDP送信機: UDPで温度値と湿度値を送信します。(外付けセンサ = SHT40)
# Copyright (c) 2021-2025 Wataru KUNINO

import socket                                               # ソケットの組み込み
from time import sleep                                      # スリープの組み込み
from lib_humiSensorSHT4 import HumiSensor                   # センサ組み込み

port = 1024                                                 # ポート番号を代入
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)     # ソケットを作成
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST,1)   # ブロードキャスト

humiSensor = HumiSensor()                                   # センサの実体化

while True:                                                 # 繰り返し構文
    (temp, humi) = humiSensor.get()                         # 温度と湿度値を取得
    udp = 'humid_1,' + str(round(temp, 1)) + ', '           # 送信文字列を生成
    udp += str(round(humi, 2)) + '\n'                       # 湿度値を追加
    sock.sendto(udp.encode(),('255.255.255.255',port))      # UDP送信
    print('send :', udp, end='')                            # 送信データを出力
    sleep(10)                                               # 10秒の待ち時間処理
sock.close()                                                # 切断(実行されない)

'''
pi@raspberrypi:~/udp/learning $ ./ex3_tx_humi.py
send : humid_1,29.7, 56.13
send : humid_1,29.7, 56.18
send : humid_1,29.7, 56.18
send : humid_1,29.7, 56.14
send : humid_1,29.7, 56.14
'''
