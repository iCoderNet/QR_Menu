
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
        if not user.is_authenticated:
            if user is not None:
                login(request, user)
                if remember :
                    request.session.set_expiry(1209600)
                    # admin 1->8

                else:
                    request.session.set_expiry(0)
                    
                return redirect('admin-dashboard')
            else:
                return render(request, 'admin_pages/login/index.htm', {'error': 'Login xato', 'username': username, 'password': password})
        else:
            return redirect('admin-dashboard')
    return render(request, 'admin_pages/login/index.htm')



@login_required(login_url='/admin/login/')
def admin_dashboard(request):
    return render(request, 'dashboard_pages\html/vertical-menu-template\index.html')
    # return render(request, 'admin_dashboard.html')
@login_required(login_url='/admin/login/')
def admin_logout(request):
    logout(request)
    return redirect('admin-logout')


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
