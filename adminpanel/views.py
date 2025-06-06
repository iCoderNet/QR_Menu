
from django.shortcuts import render, redirect, HttpResponse 
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def admin_login(request):
    if request.method == 'POST':
        username = request.POST.get('email-username')
        password = request.POST.get('password')
        remember= request.POST.get('remember')
        print(remember,' remember')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            if remember :
                request.session.set_expiry(1209600)
                # admin 1->8

            else:
                request.session.set_expiry(0)
                
            return redirect('admin-dashboard')
        else:
            return render(request, 'admin_pages/login/index.htm', {'error': 'Login yoki parol xato', 'username': username, 'password': password, 'remember': remember})
    
    
    if request.user.is_authenticated:
        return redirect('admin-dashboard')
    return render(request, 'admin_pages/login/index.htm')



@login_required(login_url='/admin/login/')
def admin_dashboard(request):
    return render(request, 'dashboard_pages\html/vertical-menu-template\index.html')
    # return render(request, 'admin_dashboard.html')
@login_required(login_url='/admin/login/')
def admin_logout(request):
    logout(request)
    return redirect('admin-login')
@login_required(login_url='/admin/login/')
def admin_settings(request):
    return render(request, 'dashboard_pages\html/vertical-menu-template\pages-account-settings-account.html')

@login_required(login_url='/admin/login/')
def dashboard_ecommerce(request):
    return render(request, 'dashboard_pages\html/vertical-menu-template/app-ecommerce-dashboard.html')

@login_required(login_url='/admin/login/')
def add_product(request):
    return render(request, 'dashboard_pages\html/vertical-menu-template/app-ecommerce-product-add.html')    

@login_required(login_url='/admin/login/')
def admin_profile(request):
    return render(request, 'dashboard_pages\html/vertical-menu-template/pages-profile-user.html')
# Create your views here.
'''
from django.shortcuts import render


def admin_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password'] 
        if username == 'admin' and password == 'admin':
                return render(request, 'admin_pages/login/index.htm')
    return render(request, 'admin_pages/login/index.htm')

def adminpanel(request):
        return render(request, 'admin_pages/login/index.htm')
'''
