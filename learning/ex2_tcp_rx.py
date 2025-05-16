#!/usr/bin/env python3
# coding: utf-8

# TCPを受信する
# Copyright (c) 2021-2025 Wataru KUNINO

# TCPで受信した文字列を表示します。
# ./ex2_rx.py

import socket                                               # ソケットの組み込み

port = 8080                                                 # ポート番号を代入
sock0 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   # TCP用ソケット作成
sock0.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # ポート再利用の許可
sock0.bind(('', port))                                      # ソケットに接続
sock0.listen(1)                                             # 同時接続数=1
print('Listening TCP port', port, '...')                    # ポート番号表示
(sock, sock_from) = sock0.accept()                          # アクセス待ち
print(sock_from[0], sock_from[1])                           # アクセス元の表示
tcp = sock.recv(128)                                        # 受信データの取得
print(tcp.decode())                                         # 受信データを表示
sock.close()                                                # ソケットの切断


''' ----------------------------------------------------------------------------
TCPサーバ側(★本プログラム)：
pi@raspberry:~/tcp/learning $ ./ex2_rx.py
Listening TCP port 8080 ...
127.0.0.1 59850
Ping

--------------------------------------------------------------------------------
TCPクラアント側：
pi@raspberry:~/tcp/learning $ ./ex1_tx.py
---------------------------------------------------------------------------- '''
