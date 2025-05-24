#!/usr/bin/env python3
# coding: utf-8

# TCPクライアント：TCPでデータを送信します
# Copyright (c) 2021-2025 Wataru KUNINO

# TCPで文字列'Ping'を送信します。
# ./ex1_tx.py

import socket                                               # ソケットの組み込み

port = 8080                                                 # ポート番号を代入
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)    # TCP用ソケット作成
sock.connect(('127.0.0.1', port))                           # TCP接続
tcp = 'Ping\n'                                              # 送信文字列
sock.send(tcp.encode())                                     # メッセージ送信
sock.close()                                                # ソケットの切断
