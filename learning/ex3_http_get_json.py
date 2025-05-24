#!/usr/bin/env python3
# coding: utf-8

################################################################################
# Example 03 IoT連携の基本 HTTP GET JSONデータを受信する
################################################################################

################################################################################
# トラブルシューティング
#   sock.connectの応答が無いとき
#   TimeoutError: Connection timed out が表示されるとき
# ------------------------------------------------------------------------------
# http_servのにbokunimo.netのIPv4アドレスを代入してください。
# 調べ方 $ nslookup bokunimo.net
# IPv6の場合は、ソケットのAddress family AF_INETをAF_INET6に変更してください。
################################################################################

import socket                                               # ソケットの組み込み
import json                                                 # JSON変換ライブラリ

http_serv = '210.224.185.41'                                # サーバIPアドレス
port = 80                                                   # ポート番号を代入
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)    # TCP用ソケット作成
sock.connect((http_serv, port))                             # TCP接続

http = 'GET /test.json HTTP/1.1\nHost: bokunimo.net\n\n'    # HTTPペイロード

sock.send(http.encode())                                    # HTTPリクエスト送信
res = sock.recv(1024).decode()                              # HTTPレスポンス受信
sock.close()                                                # ソケット通信の切断

i_body = res.find('\r\n\r\n')                               # HTTP BODY位置検索
body = res[i_body + 4:]                                     # HTTP BODYを収容
if i_body < 0 or len(body) == 0:                            # BODYなし時
    print(res)                                              # 応答文そのまま表示
    exit()                                                  # 終了

print(res[:i_body])                                         # HTTP Header表示
print()                                                     # 改行

res_dict = json.loads(res[i_body+4:])           # 受信データを変数res_dictへ代入
print('title :', res_dict.get('title'))         # 項目'title'の内容を取得・表示
print('descr :', res_dict.get('descr'))         # 項目'descr'の内容を取得・表示
print('state :', res_dict.get('state'))         # 項目'state'の内容を取得・表示
print('url   :', res_dict.get('url'))           # 項目'url'内容を取得・表示
print('date  :', res_dict.get('date'))          # 項目'date'内容を取得・表示
