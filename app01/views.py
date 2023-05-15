from django.http import HttpResponse, request
from django.shortcuts import render, redirect


# def index(request):
#     return HttpResponse
from app01.models import UserInfo


def index(request):
    return render(request,'index.html')

def user_list(request):
    return render(request,'user_list.html')

def user_add(request):
    return render(request,'user_add.html')


def tpl(request):
    return render(request,'tpl.html')

#重定向
def something(request):
    return redirect('https://www.baidu.com/')


def login(request):
    if request.method == 'GET':
        return render(request,'login.html')
    else:
        print(request.POST)
        return HttpResponse("登陆成功")


def info_list(request):
    #获取数据库信息
    data_list = UserInfo.objects.all() #[对象，对象，对象]


    #渲染，返回给用户
    return render(request,"info_list.html",{"data_list":data_list})


def info_add(request):
    #获取用户
    if request.method == "GET":
        return render(request,'info_add.html')

    #用户提交的数据
    user = request.POST.get("user")
    pwd = request.POST.get("pwd")
    age = request.POST.get("age")
    #添加到数据库
    UserInfo.objects.create(name=user,password=pwd,age=age)#model/userinfo类
    #跳转
    return redirect("/info/list")

def info_delete(request):
    nid = request.GET.get('nid')
    UserInfo.objects.filter(id=nid).delete()
    return redirect("/info/list")