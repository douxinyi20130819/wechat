from django.shortcuts import render,redirect,HttpResponse
from django.views.decorators.csrf import csrf_exempt
from wechatpy import parse_message,create_reply
from wechatpy.exceptions import InvalidSignatureException
from wechatpy.utils import check_signature
import hashlib

# Create your views here.
@csrf_exempt
def wexin(request):
    WEIXIN_TPKEN = 'douxinyi20130819'
    if request.method == "GET":
        signature = request.GET.get("signature",None)
        timestamp = request.GET.get("timestamp", None)
        nonce = request.GET.get("nonce", None)
        echostr = request.GET.get("echostr", None)
        token = WEIXIN_TPKEN
        try:
            check_signature(WEIXIN_TPKEN,signature,timestamp,nonce)
        except InvalidSignatureException:
            echostr = 'error'
        return HttpResponse(echostr,content_type="text/plain")
    elif request.method == "POST":
        msg = parse_message(request.body)
        if msg.type == 'text':
            repr = create_reply('这是条文字消息', msg)
        elif msg.type == 'image':
            repr = create_reply('这是条图片消息', msg)
        elif msg.type == 'voice':
            repr = create_reply('这是条语音消息', msg)
        else:
            repr = create_reply('这是条其他类型消息', msg)
        return HttpResponse(repr.render(),content_type='application/xml')
    else:
        pass



