#!/usr/bin/env python3
# coding: utf-8

# UDPでリソース使用率を送信します。
# Copyright (c) 2021-2025 Wataru KUNINO

# Windowsの場合はPowerShellから下記を実行してください
# pip install psutil

# ブロードキャストIPアドレスに255.255.255.255が使用できない場合は、
# 同一セグメント内のブロードキャストIPアドレスに修正してください。
# (例えば192.168.1.0/24のセグメントの場合は、末尾255にした'192.168.1.255')

import socket                                               # ソケットの組み込み
import psutil                                               # システム情報取得
from time import sleep                                      # スリープの組み込み

port = 1024                                                 # ポート番号を代入
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)     # ソケットを作成
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST,1)   # ブロードキャスト

def system_info():                                          # リソース使用率取得
    return {                                                # 下記の値を応答する
        "cpu_percent": psutil.cpu_percent(),                # CPU使用率(%)
        "memory": psutil.virtual_memory()._asdict(),        # メモリ使用率(%)
        "disk_usage": psutil.disk_usage('/')._asdict()      # ディスク使用率(%)
    }

while True:                                                 # 繰り返し構文
    info = system_info()                                    # システム情報を取得
    cpu = round(info.get('cpu_percent'))                    # CPU負荷を取得
    mem = round(info.get('memory').get('percent'))          # メモリ使用量
    disk = round(info.get('disk_usage').get('percent'))     # ディスク使用量
    udp = 'cpu_m_1,'+str(cpu)+', '+str(mem)+', '+str(disk)+'\n' # 送信データ生成
    sock.sendto(udp.encode(),('255.255.255.255',port))      # UDP送信
    print('send :', udp, end='')                            # 送信データを出力
    sleep(10)                                               # 10秒の待ち時間処理
sock.close()                                                # 切断(実行されない)
