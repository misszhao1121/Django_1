# 返回用户请求 HttpResponse
from datetime import date
# from django.contrib.redirects.models import Redirect
from django.http import request, JsonResponse, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, render_to_response
from django.shortcuts import render, HttpResponse
from django.template import RequestContext
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from app1.models import UserIPInfo, Genre, BrowseInfo,BookInstance
import json
from Django_1.util.tools import sendmail
# 导入日志
import logging

# 得到设置的日志名，即setting中的loggers的键值
logger = logging.getLogger('django')


# 测试接口
def hellword(request):
    # print(request.methon)
    a = request.methon
    return HttpResponse('你好')


# 获取用户ip,及浏览器信息接口
@csrf_exempt
def user_info(request):
    # 获取用户地址信息，META字典格式数据
    ip_addr = request.META['REMOTE_ADDR']
    user_ua = request.META['HTTP_USER_AGENT']
    server_port = request.META['SERVER_PORT']
    now_date = date.today()
    print(server_port)

    user_obj = UserIPInfo.objects.filter(ip=ip_addr)
    if ip_addr in user_obj:
        res = UserIPInfo.objects.create(ip=ip_addr, port=server_port)
        ip_add_id = res.id
    else:
        logger.info("%s alredy exists!" % (ip_addr))  # 输出日志并记录ip
        ip_add_id = user_obj[0].id

    BrowseInfo.objects.create(useragent=user_ua, ip_id=ip_add_id, uip=ip_addr)
    # 查询ip为127.0.0.1的记录并统计其条数
    ip_count = BrowseInfo.objects.filter(uip=request.POST.get('IP')).count()
    logger.info("%s sql insert: insert userinfo(useragent,userip_id)" % (user_ua))
    result = {"STATUS": "success",
              "INFO": "User info",
              "IP": ip_addr,
              'UA': user_ua,
              'SERVER_PORT': server_port,
              'date': now_date,
              'ip_count': ip_count}
    # return HttpResponse(json.dumps(result), content_type="application/json")
    return render(request, 'indexl.html', context=result)


# 信息接口实现
def user_history(request):
    # 获取UserIPInfo模型的所有对象，获取UserIPInfo的所有字段值
    # 通过获取数据库里面的ip字段值
    ip_list = UserIPInfo.objects.all()
    # print(type(ip_list))
    # print(ip_list)
    # 声明字典类型
    infos = {}
    for item in ip_list:
        # 通过userip_id外键获取相同ip的useragent，作为字典的值，ip作为键。，相当于sql查询如：select ip from userinfo where userip_id = userinfo.id,多表查询。
        infos[item.ip] = [b_obj.useragent for b_obj in BrowseInfo.objects.filter(ip_id=item.id)]
        # print(infos)

        result = {
            "STATUS": "success",
            "INFO": infos,
        }
    # json格式返回http请求
    # 调用发送邮件工具
    # resultstr = str(result)
    # sendm = sendmail(receive_addr=["542275297@qq.com"], sub_info="op ve test", content_info=resultstr)
    # sendm.send()
    # logger.info("%s error" %(sendm))
    return HttpResponse(json.dumps(result), content_type="application/json")

@csrf_exempt
def geturl(request):
    request.encoding = 'utf-8'
    IP = request.POST.get('IP')
    print(IP)
    if not IP:
        result = {
            'status': 'Failed'
        }
    else:
        result = {
            'status': 'SUCCESS',
            'IP': IP
        }
    # return render(request,'indexl.html')
    # return HttpResponseRedirect(reverse('index.html'))
    # return redirect('indexl.html')
    # return render(request, 'indexl.html', context=result)
    return render(request, 'indexl.html', context=result)

    # return HttpResponse(request)


#
# def posturl(IP):
#     result = {
#         'IP':IP
#     }
#     return render(request, 'indexl.html', context=result)
#
@csrf_exempt
def app(request):
    print('------------')
    return render(request,'index.html')
