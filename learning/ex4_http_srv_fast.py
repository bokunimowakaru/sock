#!/usr/bin/env python3
# coding: utf-8

# HTTPサーバで受信と送信を行う FastAPI版
# Copyright (c) 2022-2025 Wataru KUNINO

# FastAPIのインストール方法：
# pip install fastapi
# pip install uvicorn

# 参考文献
# https://fastapi.tiangolo.com/tutorial/first-steps/

import uvicorn
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def json():
    return '<html>Hello! <a href="json">Json</a></html>'

@app.get("/json")
async def json():
    return {'message':'Hello!'}

uvicorn.run(app, port=8080)
