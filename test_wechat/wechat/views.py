from django.shortcuts import render,redirect,HttpResponse
from django.views.decorators.csrf import csrf_exempt
import wechat
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
        if token and timestamp and nonce:
            tmp_list = [token, timestamp, nonce]
            tmp_list.sort()
            string = ''.join(tmp_list).encode('utf-8')
            string = hashlib.sha1(string).hexdigest()
            if string == signature:
                return HttpResponse(echostr)
            else:
                return HttpResponse("error")
        return HttpResponse("connect is none")


