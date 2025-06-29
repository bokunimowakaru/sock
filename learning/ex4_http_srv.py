#!/usr/bin/env python3
# coding: utf-8

# 実験用 HTTP サーバ: ブラウザから TCP 接続があると HTML コンテンツを送信します
# Copyright (c) 2022-2025 Wataru KUNINO

import socket                                               # ソケットの組み込み

port = 8080                                                 # ポート番号を代入
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)    # TCP用ソケット作成
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # ポート再利用の許可
sock.bind(('', port))                                       # ソケットに接続
sock.listen(1)                                              # 同時接続数=1
print('Listening TCP port', port, '...')                    # ポート番号表示
(client, addr) = sock.accept()                              # アクセス待ち
print(addr[0], addr[1])                                     # アクセス元の表示
tcp = client.recv(1024)                                     # 受信データの取得
print(tcp.decode().strip())                                 # 受信結果の表示
head = 'HTTP/1.0 200 OK\r\nContent-type: text/html\r\n'     # HTTPヘッダ
body = '<html>Hello!</html>\r\n'                            # HTTPボディ
client.send((head + '\r\n' + body + '\r\n').encode())       # 応答メッセージ送信
client.shutdown(socket.SHUT_WR)                             # 切断要求(FIN)送信)
sock.close()                                                # ソケットの切断
