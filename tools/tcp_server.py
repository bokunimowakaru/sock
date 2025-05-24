#!/usr/bin/env python3
# coding: utf-8

# TCPを受信する
# Copyright (c) 2021-2025 Wataru KUNINO

# TCPで受信した文字列を表示します。
# ./ex2_rx.py

import socket                                               # ソケットの組み込み
timeout = 600                                               # タイムアウト10分

def receive(client):
    n = 0                                                   # 受信データ総量
    while True:                                             # データ受信
        tcp = client.recv(1024)                             # 受信データの取得
        if len(tcp) == 0:                                   # 受信データなし時
            break                                           # ループを抜ける
        n += len(tcp)                                       # 受信データ量
        print(tcp.decode())                                 # 受信データを表示
    return n

port = 8080                                                 # ポート番号を代入
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)    # TCP用ソケット作成
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # ポート再利用の許可
sock.settimeout(timeout)                                    # タイムアウト設定
sock.bind(('', port))                                       # ソケットに接続
sock.listen(1)                                              # 同時接続数=1
client = None                                               # 未接続状態を保持
print('Listening TCP port', port, '...')                    # ポート番号表示
try:
    (client, sock_from) = sock.accept()                     # アクセス待ち
    client.settimeout(timeout)                              # タイムアウト設定
    print('Receiving from', sock_from[0], sock_from[1])     # アクセス元の表示
    n = receive(client)                                     # 関数receiveを実行
    print(n, 'Bytes Received')                              # 受信データ数を確認
except KeyboardInterrupt:                                   # キーボード割り込み
    print('Keyboard Interrupted')
except TimeoutError:                                        # タイムアウト時
    print('Timed Out')
try:
    if client:                                              # データ受信
        print('Sending FIN...')
        client.shutdown(1)                                  # 切断要求(FIN)送信
        receive(client)                                     # 関数receiveを実行
except KeyboardInterrupt:                                   # キーボード割り込み
    print('Keyboard Interrupted')
except TimeoutError:                                        # タイムアウト時
    print('Timed Out')
print('Closing Socket...')
sock.close()                                                # ソケットの切断
print('Done')
