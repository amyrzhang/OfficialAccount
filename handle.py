# -*- coding: utf-8 -*-# 
# filename: handle.py
import hashlib
import reply
import receive
import web
class Handle(object):
    def POST(self):
        try:
            webData = web.data()
            print "Handle Post webdata is ", webData
            #后台打日志
            recMsg = receive.parse_xml(webData)
            if isinstance(recMsg, receive.Msg) and recMsg.MsgType == 'text':
                toUser = recMsg.FromUserName
                fromUser = recMsg.ToUserName
                content = "您好，留言已收到，感谢您的来信📨，人工服务时间：8:30-17:30，届时客服将与您取得联系，请保持通信畅通，谢谢您的理解与支持"
                replyMsg = reply.TextMsg(toUser, fromUser, content)
                return replyMsg.send()
            else:
                print "暂且不处理"
                return "success"
        except Exception, Argment:
            return Argment
