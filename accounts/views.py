from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import auth,User
def login(request):
    if request.method == "POST":
        lemail = request.POST['lemail']
        lpass = request.POST['lpass']
        if User.objects.filter(email=lemail).exists():
            u = User.objects.get(email=lemail)
            user = auth.authenticate(username=u,password=lpass)
            if user is not None:
             auth.login(request,user)
             return redirect('/workout')
            else:
             messages.error(request,"Invalid Credentials")
             return redirect('/')
        else:
            messages.error(request,"Invalid Credentials")
            return redirect('/')
    else:
        return "Not allowed"    

def signup(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['pass']
        if User.objects.filter(email=email).exists():
            messages.warning(request,'Email-id already taken')
            return redirect('/')
        else:    
            n = name.replace(" ", "_")
            user = User.objects.create_user(username=n, password=password, email=email, first_name=name)
            user.save();
            messages.success(request,'Signedup successfully')
            return redirect('/')
    else:
        return "Not allowed"    

def visitor_ip_address(request):

    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')

    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip  

def profile(request):
    ip = visitor_ip_address(request)
    return render(request,'profile.html',{'ip':ip})

def logout(request):
    auth.logout(request)
    return redirect('/')     

def change(request):
    if request.method == "POST":
        old = request.POST['old']
        new = request.POST['new']
        user = request.user
        cuser = auth.authenticate(username=user, password=old)
        if cuser is not None:
            cus = User.objects.get(username__exact=user)
            cus.set_password(new)
            cus.save()
            messages.success(request,'Your Password is changed successfully')
            auth.login(request,user)
        return redirect(profile)
    else:
        return "Not allowed" 