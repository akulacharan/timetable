from django.shortcuts import render,redirect,HttpResponse
from .models import TimeTable
from django.contrib.auth.models import User,auth
from django.http import JsonResponse
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt


def register(request):
    if request.method=='POST':
        username=request.POST['username']
        email = request.POST['email']
        password=request.POST['password']
        confirm_password = request.POST['confirm-password']

        if User.objects.filter(username=username).exists():
            return HttpResponse("<script>alert('username taken')</script>")
            #messages.info(request,'username-taken')
        elif User.objects.filter(email=email).exists():
            return HttpResponse("<script>alert('email taken')</script>")
            #messages.info(request, 'email-taken')

        elif confirm_password != password:
            return HttpResponse("<script>alert('password doesnot matched')</script>")

        else:
            user=User.objects.create_user(username=username,password=password,email=email)
            user.save();
            student = TimeTable.objects.create(username=username,email=email)
            student.save()
            messages.info(request, 'user-created')
        return redirect('/login')
    return render(request,'register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            return HttpResponse('wrong username / password')
            messages.info(request, 'invalid credentials')
    else:
        return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def table(request,id):
    global g
    g = id
    content = TimeTable.objects.get(id=g)
    return render(request,'timetable.html',{'content':content})

def home(request):
    context = TimeTable.objects.all()
    return render(request,'base.html',{'context':context})

@csrf_exempt
def savestudent(request):
    ide=request.POST.get('id','')
    type=request.POST.get('type','')
    value=request.POST.get('value','')
    student=TimeTable.objects.get(id=g)
    # for timings
    if type == "tm1":
        student.tm1=value
    if type == "tm2":
        student.tm2 = value
    if type == "tm3":
        student.tm3 = value
    if type == "tm4":
        student.tm4 = value
    if type == "tm5":
        student.tm5 = value
    if type == "tm6":
        student.tm6 = value
    if type == "tm7":
        student.tm7 = value
    if type == "tm8":
        student.tm8 = value
    # on monday
    if type == "m1":
        student.m1 = value
    if type == "m2":
        student.m2 = value
    if type == "m3":
        student.m3 = value
    if type == "m4":
        student.m4 = value
    if type == "m5":
        student.m5 = value
    if type == "m6":
        student.m6 = value
    if type == "m7":
        student.m7 = value
    if type == "m8":
        student.m8 = value
    # on tuesday
    if type == "tu1":
        student.tu1 = value
    if type == "tu2":
        student.tu2 = value
    if type == "tu3":
        student.tu3 = value
    if type == "tu4":
        student.tu4 = value
    if type == "tu5":
        student.tu5 = value
    if type == "tu6":
        student.tu6 = value
    if type == "tu7":
        student.tu7 = value
    # on wednesday
    if type == "w1":
        student.w1 = value
    if type == "w2":
        student.w2 = value
    if type == "w3":
        student.w3 = value
    if type == "w4":
        student.w4 = value
    if type == "w5":
        student.w5 = value
    # ON THURSDAY
    if type == "th1":
        student.th1 = value
    if type == "th2":
        student.th2 = value
    if type == "th3":
        student.th3 = value
    if type == "th4":
        student.th4 = value
    if type == "th5":
        student.th5 = value
    if type == "th6":
        student.th6 = value
    if type == "th7":
        student.th7 = value
    # ON FRIDAY
    if type == "f1":
        student.f1 = value
    if type == "f2":
        student.f2 = value
    if type == "f3":
        student.f3 = value
    if type == "f4":
        student.f4 = value
    if type == "f5":
        student.f5 = value
    if type == "f6":
        student.f6 = value
    if type == "f7":
        student.f7 = value
    # ON SATURDAY
    if type == "s1":
        student.s1 = value
    if type == "s2":
        student.s2 = value
    if type == "s3":
        student.s3 = value
    if type == "s4":
        student.s4 = value
    if type == "s5":
        student.s5 = value

    student.save()
    return JsonResponse({"success": "Updated"})