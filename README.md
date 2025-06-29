# sock
ソケット通信サンプル・プログラム集

## Lesson 1 TCP クライアント

TCP でデータを送信します。  
### [ex1_tcp_tx.py](learning/ex1_tcp_tx.py)  


## Lesson 2 TCP サーバ

TCP データを受信し、表示します。  
### [ex2_tcp_rx.py](learning/ex2_tcp_rx.py)  


## Lesson 3 HTTP クライアント

HTTP GET で HTML データを受信します。  
### [ex3_http_get.py](learning/ex3_http_get.py)  


## Lesson 4 実験用 HTTP サーバ

ブラウザから TCP 接続があると HTML コンテンツを送信します。  
### [ex4_http_srv.py](learning/ex4_http_srv.py)  


## Lesson 5 UDP 送信機

UDP で 文字列 'Ping' を送信します。  
### [ex5_udp_tx.py](learning/ex5_udp_tx.py)  


## Lesson 6 UDP 受信機

UDP で受信した文字列を表示します。  
### [ex6_udp_rx.py](learning/ex6_udp_rx.py)  


## Lesson 7 リソース使用率送信機

UDPでリソース使用率を送信します。  
### [ex7_udp_tx_cpu.py](learning/ex7_udp_tx_cpu.py)  


## Lesson 8 センサ用UDP送信機

UDPで温度値と湿度値を送信します。(外付けセンサ = SHT30)  
### [ex8_udp_tx_humi.py](learning/ex8_udp_tx_humi.py)  

センサ用UDP送信機: UDPで温度値を送信します。(外付けセンサ不要)  
### [ex8_udp_tx_temp.py](learning/ex8_udp_tx_temp.py)  

