#!/usr/bin/env python3
# coding: utf-8

# TCPを受信する
# Copyright (c) 2021-2025 Wataru KUNINO

# TCPの待ち受けと、受信した文字列の表示を繰り返します。
# ex2_rx.pyとの違いは、一度、実行すると繰り返し動作し続ける点と、
# Listening TCP portや、送信元を表示しない点です。
# ./ex2_rx_loop.py

# 受信データをファイルに保存し続けることも出来ます。
# ./ex2_rx_loop.py > log.csv &

import socket                                               # ソケットの組み込み

port = 8080                                                 # ポート番号を代入
sock0 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   # TCP用ソケット作成
sock0.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # ポート再利用の許可
sock0.bind(('', port))                                      # ソケットに接続
sock0.listen(3)                                             # 同時接続数=3
# print('Listening TCP port', port, '...')                  # ポート番号表示

while True:                                                 # 繰り返し構文
    (sock, sock_from) = sock0.accept()                      # アクセス待ち
    # print(sock_from[0], sock_from[1])                     # アクセス元の表示
    tcp = sock.recv(128)                                    # 受信データの取得
    print(tcp.decode().strip(), flush=True)                 # 受信データを表示
    sock.close()                                            # 切断

''' ----------------------------------------------------------------------------
TCPサーバ側(★本プログラム)：
pi@raspberry:~/tcp/learning $ ./ex2_rx_loop.py
Ping
Ping
Ping

--------------------------------------------------------------------------------
TCPクラアント側：
pi@raspberry:~/tcp/learning $ ./ex1_tx.py
pi@raspberry:~/tcp/learning $ ./ex1_tx.py
pi@raspberry:~/tcp/learning $ ./ex1_tx.py
---------------------------------------------------------------------------- '''
