#!/usr/bin/python
#-*-coding: utf-8 -*-
##from __future__ import absolute_import
###
from flask import Flask, jsonify, render_template, request
import json

#import pymongo
#from pymongo import MongoClient
#from flask_restful import Resource, Api, reqparse

from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,TemplateSendMessage,ImageSendMessage, StickerSendMessage, AudioSendMessage
)
from linebot.models.template import *
from linebot import (
    LineBotApi, WebhookHandler
)

app = Flask(__name__)

lineaccesstoken = 'RcBxylbH372xJfChROOpZxoInwYQykvtus6O1E+fHCQ9bO5pGIDYk8xaYfpNLkDRY3XW/VyPerpdC+OVe3j0oMRUelVx22qVz0dmOvk56WF6K6V2hw7Ns4aBTDFb8yeTyUPgCNwwrMB7jyPikc9AdAdB04t89/1O/w1cDnyilFU='
line_bot_api = LineBotApi(lineaccesstoken)

####################### new ########################
@app.route('/')
def index():
    return "Hello World!"


@app.route('/callback', methods=['POST'])
def callback():
    #try:
    json_line = request.get_json(force=False,cache=False)
    #except:
    #    print('cannot get json_line')
    #    return '',200
    json_line = json.dumps(json_line)
    decoded = json.loads(json_line)
    no_event = len(decoded['events'])
    for i in range(no_event):
        event = decoded['events'][i]
        #try:
        event_handle(event)
        #except:
        #    pass
    return '',200


def event_handle(event):
    print(event)
    try:
        userId = event['source']['userId']
    except:
        print('error cannot get userId')
        return ''

    try:
        rtoken = event['replyToken']
    except:
        print('error cannot get rtoken')
        return ''
    try:
        msgId = event["message"]["id"]
        msgType = event["message"]["type"]
    except:
        print('error cannot get msgID, and msgType')
        sk_id = np.random.randint(1,17)
        replyObj = StickerSendMessage(package_id=str(1),sticker_id=str(sk_id))
        line_bot_api.reply_message(rtoken, replyObj)
        return ''
#
    if msgType == "text":
        msg = str(event["message"]["text"])
        outmsg = textmessagehandler(msg)
        replyObj = TextSendMessage(text=outmsg)
        line_bot_api.reply_message(rtoken, replyObj)

    else:
        replyObj = StickerSendMessage(package_id=str(1),sticker_id=str(sk_id))
        line_bot_api.reply_message(rtoken, replyObj)
    return ''

def textmessagehandler(msg):
    return msg

if __name__ == '__main__':
    app.run(debug=True)
