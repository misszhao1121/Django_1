# 返回用户请求 HttpResponse
from django.http import request,JsonResponse,HttpResponse
from django.shortcuts import render
from django.shortcuts import render,HttpResponse
import  logging
# Create your views here.
from app1.models import *
import json
from Django_1.util.tools import sendmail
logger = logging.getLogger('django')
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
    user_obj = UserIPInfo.objects.filter(ip=ip_addr,port=server_port)
    if ip_addr in user_obj:
        res = UserIPInfo.objects.create(ip=ip_addr,port = server_port)
        ip_add_id = res.id
    else:
        logger.info("%s alredy exists!"%(ip_addr))   #输出日志并记录ip
        ip_add_id = user_obj[0].id

    BrowseInfo.objects.create(useragent = user_ua,userip_id = ip_add_id)
    logger.info("%s sql insert: insert userinfo(useragent,userip_id)"%(user_ua))
    result = {"STATUS":"success",
              "INFO":"User info",
              "IP":ip_addr,
              'UA':user_ua,
              'SERVER_PORT':server_port}
    return HttpResponse(json.dumps(result),content_type="application/json")

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
        infos[item.ip] = [ b_obj.useragent for b_obj in BrowseInfo.objects.filter(userip_id = item.id)]
        # print(infos)

        result = {
            "STATUS":"success",
            "INFO":infos,
        }
    # json格式返回http请求
    # 调用发送邮件工具
    # resultstr = str(result)
    # sendm = sendmail(receive_addr=["542275297@qq.com"], sub_info="op ve test", content_info=resultstr)
    # sendm.send()
    # logger.info("%s error" %(sendm))
    return  HttpResponse(json.dumps(result),content_type="application/json")
