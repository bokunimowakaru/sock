#!/usr/bin/env python3
# coding: utf-8

# TCPサーバ：TCPデータを受信し、表示します
# Copyright (c) 2021-2025 Wataru KUNINO

import socket                                               # ソケットの組み込み

port = 8080                                                 # ポート番号を代入
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)    # TCP用ソケット作成
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # ポート再利用の許可
sock.bind(('', port))                                       # ソケットに接続
sock.listen(1)                                              # 同時接続数=1
print('Listening TCP port', port, '...')                    # ポート番号表示
(client, sock_from) = sock.accept()                         # アクセス待ち
print(sock_from[0], sock_from[1])                           # アクセス元の表示
tcp = client.recv(128)                                      # 受信データの取得
print(tcp.decode())                                         # 受信データを表示
client.shutdown(socket.SHUT_WR)                             # 切断要求(FIN)送信)
sock.close()                                                # ソケットの切断

''' ----------------------------------------------------------------------------
TCPサーバ側(★本プログラム)：
Listening TCP port 8080 ...
127.0.0.1 59850
Ping

--------------------------------------------------------------------------------
TCPクラアント側プログラムは、ex1_tcp_tx.py
---------------------------------------------------------------------------- '''
