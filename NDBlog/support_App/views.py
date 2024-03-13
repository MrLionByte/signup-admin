from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth import authenticate,login as auth_login,logout
from django.contrib.auth.models import User
from django.views.decorators.cache import never_cache
from django.contrib.auth.decorators import login_required,user_passes_test
from django.contrib import messages,auth
from django.http import JsonResponse
from django.db.models import Q

# Create your views here.

@never_cache
def aboutpage(request):
    if request.user.is_authenticated:
        return redirect('blogpage')
    return render(request,"about.html")

check_alpha_list=list(map(chr, range(97, 123)))
check_symbol_list=["-","_"]

@never_cache
def signup(request):
    if request.user.is_authenticated:
        return redirect('blogpage')
    if request.method=="POST":
        firstname=request.POST.get('fname')
        lastname=request.POST.get('lname')
        user_name=request.POST.get('username')
        user_email=request.POST.get('email')
        user_password=request.POST.get('password1')
        confirm_password=request.POST.get('password2')
        if User.objects.filter(username=user_name).exists():
            messages.error(request,"Username already exist")
        elif user_email==user_name or '@' in user_name:
            messages.error(request,"Username can't be Email")
        else:
            if user_name[0]=="-" or user_name[len(user_name)-1]=="-" or " " in user_name or " " in firstname:
                messages.error(request,"username not acceptable")
                return render(request,"signup.html")
            elif len(user_password)<8:
                messages.error(request,"password must be at least 8 characters")
                return render(request,"signup.html")
            else:
                if user_password==confirm_password:
                    new_user=User.objects.create_user(user_name,user_email,user_password)
                    new_user.first_name=firstname
                    new_user.last_name=lastname
                    new_user.save()
                    messages.success(request,"User created successfully")
                else:
                    messages.error(request,"password mismatching")
    return render(request,"signup.html")


@never_cache
def login(request):
    if request.user.is_authenticated:
        return redirect('blogpage')
    if request.method=="POST":
       check_username=request.POST.get('username')
       check_password=request.POST.get('password')
       user_object=authenticate(request,username=check_username,password=check_password)
       print(user_object)
       if user_object is not None: 
           auth_login(request,user_object)
           return redirect('blogpage')
       else:
           messages.error(request,'incorrect password or username') 
    return render(request,"signin.html")

def blogpage(request):
    if request.user.is_authenticated:
        return render(request,'blogpage.html')
    return redirect('login')

def logout_action(request): 
    if request.user.is_authenticated:
        logout(request)
        return redirect('/')

def terms(request):
    return render(request,'terms.html')

@never_cache
def admin_login(request):
    if request.user.is_authenticated:
        return redirect("admin_panel")
    if request.method=='POST':
        check_username=request.POST.get('admin_name')
        check_password=request.POST.get('admin_password')
        user_object=authenticate(request,username=check_username,password=check_password)
        if user_object is not None: 
                auth_login(request,user_object)
                return redirect('admin_panel')
        else:
                messages.error(request,'incorrect password or username')
                return redirect('admin_login')
    return render(request,'adminLogin.html')


def admin_panel(request):
    if request.user.is_superuser:
        search_query = request.GET.get('search', '')
        if search_query:
            data = User.objects.filter(
                Q(username__icontains=search_query) |
                Q(email__icontains=search_query) |
                Q(first_name__icontains=search_query) |
                Q(last_name__icontains=search_query)
            )
        else:
            data = User.objects.all()

        context = {
            'data': data,
            'search_query': search_query,
        }
        return render(request, 'adminpanel.html', context)

    messages.error(request, "Only admin is permitted")
    return redirect('admin_login')


def admin_add(request):
    if request.method=="POST":
        firstname=request.POST.get('firstname')
        lastname=request.POST.get('lastname')
        email=request.POST.get('email')
        username=request.POST.get('username')
        password=request.POST.get('password')
        data= User.objects.create_user(
                first_name=firstname,
                last_name=lastname,
                username=username,
                email=email,
                password=password
            )
        try:
            data.save()
            return redirect("admin_panel")
        except:
            return redirect("admin_panel")

def admin_edit(request):
    data=User.objects.all()
    context={
        'data':data
    }
    return redirect("admin_panel",context)
 
def admin_update(request):
    if request.method=="POST":
        user_id = request.POST.get('user_id')
        try:
                user = User.objects.get(id=user_id)
                user_id = user.pk
                user_name=request.POST.get('username')
                email=request.POST.get('email')
                firstname=request.POST.get('firstname')
                lastname=request.POST.get('lastname')
                data=User.objects.get(id=user_id)
                data.username=user_name
                data.first_name=firstname
                data.last_name=lastname
                if email:
                    data.email = email
                data.save()
                return redirect("admin_panel")
        except User.DoesNotExist:
            return redirect("admin_panel")
    else:
        data=User.objects.all()
        context={
        'data':data
             }
        return redirect("admin_panel",context)
   
 
def admin_delete(request):
    if request.method =='POST':
        username=request.POST.get('username')
        try:
            data_delete=User.objects.get(username=username)
            data_delete.delete()
        except User.DoesNotExist:
            pass
    return redirect('admin_panel')


def admin_logout(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('/')
