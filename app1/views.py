
from django.http import request,JsonResponse,HttpResponse
# 返回用户请求 HttpResponse
from django.shortcuts import render
from django.shortcuts import render,HttpResponse

# Create your views here.
from app1.models import *
import json

# 测试接口
def hellword(request):
    # print(request.methon)
    a = request.methon
    return HttpResponse('你好')

# 获取用户ip,及浏览器信息接口
def user_info(request):
    # 获取用户地址信息，META字典格式数据
    ip_addr = request.META['REMOTE_ADDR']
    user_ua = request.META['HTTP_USER_AGENT']
    server_port = request.META['SERVER_PORT']

    print(server_port)

    user_obj = UserIPInfo.objects.filter(ip = ip_addr,port = server_port)
    if not user_obj:
        res = UserIPInfo.objects.create(ip = ip_addr,port = server_port)

        ip_add_id = res.id
    else:
        ip_add_id = user_obj[0].id

    BrowseInfo.objects.create(useragent = user_ua,userip_id = ip_add_id)

    result = {"STATUS":"success",
              "INFO":"User info",
              "IP":ip_addr,
              'UA':user_ua,
              'SERVER_PORT':server_port}
    return HttpResponse(json.dumps(result),content_type="application/json")

# 信息接口实现
def user_history(request):
    # 获取UserIPInfo模型的所有对象，获取UserIPInfo的所有字段值
    ip_list = UserIPInfo.objects.all()
    # 声明字典类型
    infos = {}
    for item in ip_list:
        # 通过userip_id外键获取相同ip的useragent，作为字典的值，ip作为键。
        infos[item.ip] = [ b_obj.useragent for b_obj in BrowseInfo.objects.filter(userip_id = item.id)]
        # print(infos)

    result = {
        "STATUS":"success",
        "INFO":infos,
    }
    # json格式返回http请求
    return  HttpResponse(json.dumps(result),content_type="application/json")
