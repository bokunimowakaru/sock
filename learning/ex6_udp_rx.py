#!/usr/bin/env python3
# coding: utf-8

# UDP受信機: UDPで受信した文字列を表示します。
# Copyright (c) 2021-2025 Wataru KUNINO

import socket                                               # ソケットの組み込み

port = 1024                                                 # ポート番号を代入
sock=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)       # ソケットを作成
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)   # オプション設定
print('Listening UDP port', port, '...')                    # ポート番号表示

sock.bind(('', port))                                       # ポート番号を設定
udp = sock.recvfrom(128)                                    # UDPパケットを取得
print(udp[1], udp[0].decode())                              # 受信データを表示
sock.close()                                                # ソケットの切断
