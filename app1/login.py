from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt

from app1.models import K_USER
from app1.views import ywweb


@csrf_exempt
def login(request):
    username = request.POST.get('username',None)
    password = request.POST.get('password',None)
    # 确保当数据请求中没有username键时不会抛出异常，而是返回一个我们指定的默认值None；
    message = {
        'failed':"您还未注册，请去注册",
        'success':"登陆成功"
    }
    try:
        userinfo = K_USER.objects.get(username=username)
    except:
        return render(request, 'login.html',context=message)

    if userinfo.password == password:
        result = {
            'username': userinfo.username,
            'password': userinfo.password,
            'failed':"您还未注册，请去注册",
            'success':"登陆成功"
        }
        return render(request, 'ywweb.html', context=result)
    else:
        return render(request, 'login.html')


# 注册函数
def regist(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    if not K_USER.objects.filter(username=username):
        K_USER.objects.create(username=username, password=password)
        print("创建了" + username)
        return HttpResponse("创建了" + username)
    else:
        return HttpResponse(username + "用户已经存在")
