#!/usr/bin/env python3
# coding: utf-8

################################################################################
# 温湿度センサ SENSIRION SHT40 から温度と湿度を取得します。
# sht4-bsd3clause/sht4x_i2c を使用します
#
#                                               Copyright (c) 2025 Wataru KUNINO
################################################################################

import subprocess

class HumiSensor:                                       # クラスHumiSensorの定義
    def __init__(self):                                 # コンストラクタ作成
        self.command = ['../tools/sht4-bsd3clause/sht4x_i2c'] # コマンド
        self.temp = float()                             # 温度測定結果の保持用
        self.humi = float()                             # 湿度測定結果の保持用
    def get(self):                                      # 温度値取得用メソッド
        res = subprocess.run(self.command,stdout=subprocess.PIPE)
        for line in res.stdout.decode().splitlines():
            if ':' in line:
                (item,val_s) = line.split(':', 1)
                try:
                    val = float(val_s.strip())
                except ValueError:
                    val = None
            if val is not None:
                if item == 'a_temperature':
                    self.temp = val
                if item == 'a_humidity':
                    self.humi = val
        return (self.temp, self.humi)                   # 測定結果を応答
