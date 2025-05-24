#!/usr/bin/env python3
# coding: utf-8

# 簡易HTTPサーバ
# Copyright (c) 2022-2025 Wataru KUNINO

import socket                                               # ソケットの組み込み

port = 8080                                                 # ポート番号を代入
sock0 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   # TCP用ソケット作成
sock0.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # ポート再利用の許可
sock0.bind(('', port))                                      # ソケットに接続
sock0.listen(1)                                             # 同時接続数=1
print('Listening TCP port', port, '...')                    # ポート番号表示
(client, sock_from) = sock0.accept()                        # アクセス待ち
print(sock_from[0], sock_from[1])                           # アクセス元の表示
tcp = client.recv(1024)                                     # 受信データの取得
print(tcp.decode().strip())                                 # 受信結果の表示
head = 'HTTP/1.0 200 OK\r\nContent-type: text/html\r\n'     # HTTPヘッダ
body = '<html>Hello!</html>\r\n'                            # HTTPボディ
client.send((head + '\r\n' + body + '\r\n').encode())       # 応答メッセージ送信
client.shutdown(socket.SHUT_WR)                             # 切断要求(FIN)送信)
sock.close()                                                # ソケットの切断

''' ----------------------------------------------------------------------------
HTTPサーバ側(★本プログラム)：
127.0.0.1 36762
GET / HTTP/1.1
Host: 127.0.0.1:8080
User-Agent: curl/7.74.0
Accept: */*
--------------------------------------------------------------------------------
HTTPクラアント側：
curl -v 127.0.0.1:8080
*   Trying 127.0.0.1:8080...
* Connected to 127.0.0.1 (127.0.0.1) port 8080 (#0)
> GET / HTTP/1.1
> Host: 127.0.0.1:8080
> User-Agent: curl/7.74.0
> Accept: */*
>
* Mark bundle as not supporting multiuse
* HTTP 1.0, assume close after body
< HTTP/1.0 200 OK
< Content-type: text/html
<
<html>Hello!</html>

* Closing connection 0
---------------------------------------------------------------------------- '''
