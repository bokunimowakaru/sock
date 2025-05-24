#!/usr/bin/env python3
# coding: utf-8

# UDPで温度値を送信します。(外付けセンサ不要)
# Copyright (c) 2021-2025 Wataru KUNINO

# Windowsの場合はPowerShellから下記を実行してください
# pip install psutil

# Windowsの場合はブロードキャストIPアドレスに255.255.255.255が使用できないので
# brod_ipの値を同一セグメント内のブロードキャスト・IPアドレスに修正してください
# (例えば192.168.1.0/24のセグメントの場合は、末尾255にした'192.168.1.255')

import socket                                               # ソケットの組み込み
import psutil                                               # システム情報取得
from time import sleep                                      # スリープの組み込み

brod_ip = '255.255.255.255'                                 # ブロードキャストIP
port = 1024                                                 # ポート番号を代入
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)     # ソケットを作成
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST,1)   # ブロードキャスト

def system_info():
    return {
        "cpu_percent": psutil.cpu_percent(),
        "memory": psutil.virtual_memory()._asdict(),
        "disk_usage": psutil.disk_usage('/')._asdict()
    }

while True:                                                 # 繰り返し構文
    info = system_info()                                    # システム情報を取得
    cpu = round(info.get('cpu_percent'), 0)                 # CPU負荷を取得
    mem = round(info.get('memory').get('percent'), 0)       # メモリ使用量
    disk = round(info.get('disk_usage').get('percent'),0)   # ディスク使用量
    udp = 'cpu_m_1,'+str(cpu)+', '+str(mem)+', '+str(disk)+'\n' # 送信データ生成
    sock.sendto(udp.encode(),(brod_ip,port))                # UDP送信
    print('send :', udp, end='')                            # 送信データを出力
    sleep(10)                                               # 10秒の待ち時間処理
sock.close()                                                # 切断(実行されない)
