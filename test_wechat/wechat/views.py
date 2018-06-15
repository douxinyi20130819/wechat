from django.shortcuts import render,redirect,HttpResponse
import wechat
import hashlib

# Create your views here.

def wexin(request):
    WEIXIN_TPKEN = 'dou20130819'
    if request.method == "GET":
        signature = request.GET.get("signature",None)
        timestamp = request.GET.get("timestamp", None)
        nonce = request.GET.get("nonce", None)
        echostr = request.GET.get("echostr", None)
        token = WEIXIN_TPKEN
        if token and timestamp and nonce:
            tmp_list = [token, timestamp, nonce]
            tmp_list.sort()
            tmp_str = "%s%s%s" %tuple(tmp_list)
            tmp_str = hashlib.sha1(bytes(tmp_str,encoding='utf-8')).hexdigest()
            if tmp_str == signature:
                return HttpResponse(echostr)
            else:
                return HttpResponse("error")
        return HttpResponse("connect is none")


