from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt

from app1.models import K_USER
from app1.views import ywweb


@csrf_exempt
def login(request):
    username = request.POST.get('username')
    print(username)
    password = request.POST.get('password')
    userinfo = K_USER.objects.get(username=username)
    result = {
        'username':userinfo.username,
        'password':userinfo.password
    }
    print(userinfo)
    if userinfo:
        return render(request, 'ywweb.html', context=result)
        print(result)
    else:
        return False
        print(False)


def regist(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    K_USER.objects.create(username=username, password=password)
    print("创建了" + username)
    return HttpResponse("创建了" + username)
