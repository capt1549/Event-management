from django.shortcuts import render,redirect
from app.models import Events, RegisterAdmin,RegisterAdmin, RegisterUser
from django.contrib import messages
import mysql.connector
from operator import itemgetter

def INDEX(request):
    emp=Events.objects.all()
    context={
        'emp':emp
    }
    return render(request,"admin.html",context)

def Add(request):
    if request.method=="POST":
        Event=request.POST.get('event')
        Member=request.POST.get('member')
        Start=request.POST.get('start')
        End=request.POST.get('end')
        Location=request.POST.get('location')
        Profile=request.POST.get('profile')

        emp=Events.objects.create(
            event=Event,
            member=Member,
            start=Start,
            end=End,
            location=Location,
            profile=Profile,
        )
        emp.save()
        return redirect("home")
    return render(request,'admin.html')


def Edit(request):
    emp=Events.objects.all()

    context={
        'emp':emp,
    }
    return redirect(request,'admin.html',context)


def Update(request,id):
    if request.method=="POST":
        event=request.POST.get('event')
        member=request.POST.get('member')
        start=request.POST.get('start')
        end=request.POST.get('end')
        location=request.POST.get('location')
        profile=request.POST.get('profile')

        emp=Events(
            id=id,
            event=event,
            member=member,
            start=start,
            end=end,
            location=location,
            profile=profile,
        )
        emp.save()
        return redirect("home")
    return redirect(request,'admin.html')


def Delete(request,id):
    emp=Events.objects.filter(id=id)
    emp.delete()

    context={
        'emp':emp
    }
    return redirect('home')

#**************************Admin authentication****************************
def signupadmin(request):
    if request.method=="POST":
        Username=request.POST['username']
        Fname=request.POST['fname']
        Lname=request.POST['lname']
        Email=request.POST['email']
        Pass1=request.POST['pass1']
        Pass2=request.POST['pass2']
        Gender=request.POST['gender']

        if RegisterAdmin.objects.filter(username=Username):
            messages.error(request,"Username already exist! Please try another.")
            return redirect('signupuser')

        if RegisterAdmin.objects.filter(email=Email):
            messages.error(request,"Email already registered! Please try another.")
            return redirect('signupuser')

        if len(Username)>20:
            messages.error(request,"Username should not be greater than 20 characters.")
            return redirect('signupuser')

        if Pass1 != Pass2:
            messages.error(request,"Password didn't matched. ")
            return redirect('signupuser')

        if not Username.isalnum():
            messages.error(request,"Username must be a Alpha-numeric. ")
            return redirect('signupuser')

        user= RegisterAdmin.objects.create(
            username=Username,
            fname=Fname,
            lname=Lname,
            email=Email,
            pass1=Pass1,
            pass2=Pass2,
            gender=Gender,
        )
        user.save()
        return redirect('admin_login')
    else:
        return render(request,'adminsignup.html')


def loginadmin(request):
    try:
        if request.method=="POST":

            Username= request.POST['username']
            Pass1=request.POST['pass1']

            user=RegisterAdmin.objects.get(username=Username,pass1=Pass1)
            if Username:
                if user.pass1==Pass1:
                    return redirect('home')
                else:
                    messages.error(request,"Incorrect Password")
                    return redirect('signin')
            else:
                    messages.error(request,"Incorrect Username")
                    return redirect('signin')
    except:
            messages.error(request,"Bad credentials")
            return redirect('signin')

#****************************************User authentication******************************
def signupuser(request):
    if request.method=="POST":
        Username=request.POST['username']
        Fname=request.POST['fname']
        Lname=request.POST['lname']
        Email=request.POST['email']
        Pass1=request.POST['pass1']
        Pass2=request.POST['pass2']
        Gender=request.POST['gender']

        if RegisterUser.objects.filter(username=Username):
            messages.error(request,"Username already exist! Please try another.")
            return redirect('signupuser')

        if RegisterUser.objects.filter(email=Email):
            messages.error(request,"Email already registered! Please try another.")
            return redirect('signupuser')

        if len(Username)>20:
            messages.error(request,"Username should not be greater than 20 characters.")
            return redirect('signupuser')

        if Pass1 != Pass2:
            messages.error(request,"Password didn't matched. ")
            return redirect('signupuser')

        if not Username.isalnum():
            messages.error(request,"Username must be a Alpha-numeric. ")
            return redirect('signupuser')

        user= RegisterUser.objects.create(
            username=Username,
            fname=Fname,
            lname=Lname,
            email=Email,
            pass1=Pass1,
            pass2=Pass2,
            gender=Gender,
        )
        user.save()
        return redirect('signin')
    else:
        return render(request,'usersignup.html')

def loginuser(request):
    try:
        if request.method=="POST":

            Username= request.POST['username']
            Pass1=request.POST['pass1']

            user=RegisterUser.objects.get(username=Username,pass1=Pass1)
            if Username:
                if user.pass1==Pass1:
                    return redirect('user')
                else:
                    messages.error(request,"Incorrect Password")
                    return redirect('signin')
            else:
                    messages.error(request,"Incorrect Username")
                    return redirect('signin')
    except:
            messages.error(request,"Bad credentials")
            return redirect('signin')
# *********************************************************************************************************************

def signin(request):
    return render(request,"userlogin.html")

def signup(request):
    return render(request,'usersignup.html')
    
def signout(request):
    return render(request,"userlogin.html")

def user(request):
    emp=Events.objects.all()
    context={
        'emp':emp
    }
    return render(request,"admin.html",context)

def admin_login(request):
    return render(request,"adminlogin.html")

def admin_signup(request):
    return render(request,"adminsignup.html")
