#!/usr/bin/env python3
# coding: utf-8
# Example 03 IoT連携の基本 HTTP GET

import socket                                               # ソケットの組み込み
import json                                                 # JSON変換ライブラリ

http_serv = '210.224.185.41'                                # サーバIPアドレス
port = 80                                                   # ポート番号を代入
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)    # TCP用ソケット作成
sock.connect((http_serv, port))                             # TCP接続

http = 'GET /test.json HTTP/1.1\nHost: bokunimo.net\n\n'

sock.send(http.encode())                        # HTTPリクエスト送信
res = sock.recv(1024).decode()                  # HTTPレスポンス受信
sock.close()                                    # HTTPアクセスの終了

i_body = res.find('\r\n\r\n')
if i_body < 0:
    print(res)
    exit()

print(res[:i_body])
print()
res_dict = json.loads(res[i_body+4:])           # 受信データを変数res_dictへ代入
print('title :', res_dict.get('title'))         # 項目'title'の内容を取得・表示
print('descr :', res_dict.get('descr'))         # 項目'descr'の内容を取得・表示
print('state :', res_dict.get('state'))         # 項目'state'の内容を取得・表示
print('url   :', res_dict.get('url'))           # 項目'url'内容を取得・表示
print('date  :', res_dict.get('date'))          # 項目'date'内容を取得・表示
