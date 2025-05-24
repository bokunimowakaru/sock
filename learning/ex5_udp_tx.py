#!/usr/bin/env python3
# coding: utf-8

# UDPで文字列'Ping'を送信します。
# Copyright (c) 2021-2025 Wataru KUNINO

import socket                                               # ソケットの組み込み

port = 1024                                                 # ポート番号を代入
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)     # ソケットを作成
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST,1)   # ブロードキャスト
udp = 'Ping\n'                                              # 送信文字列
sock.sendto(udp.encode(),('255.255.255.255',port))          # UDP送信
sock.close()                                                # ソケットの切断
