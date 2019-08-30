from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.

def test(request):
    return render(request, 'test.html')

def login(request):
    return render(request, 'login.html')

def login_check(request):
    if request.method == 'POST':  # 是post请求就取出form表单中传过来的用户名和密码

        user_name = request.POST.get('username', '')
        pass_word = request.POST.get('password', '')
        user = authenticate(username=user_name, password=pass_word)
        # 调用authenticate函数来验证用户名和密码合法性，authenticate函数接受2个参数username和passsword
        # authenticate方法验证合法返回user对象，不合法返回None
        if user is not None:
            auth.login(request, user)  # 调用login函数完成user对象登陆，login方法传入request和user对象
            return render(request, 'home.html')  # 登陆成功返回首页
        else:
            return render(request, 'login.html', {'error': '用户名或密码错误'})
    elif request.method == 'GET':  # 是get请求直接返回login页面
        context = {}
        return render(request, 'login.html', context)


    
def home(request):
    return render(request,"home.html")

def logout(request):
    auth.logout(request)
    return render(request,'login.html')
