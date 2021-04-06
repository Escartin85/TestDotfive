from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
# View for Home Page
def home_page(request):

    context_data = {
        "Title": "Home",
    }

    return render(request, "index.html", context_data)

# View for Login Page
def login_page(request):
    if request.user.is_authenticated:
        return redirect('itemList')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password =request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('itemList')
            else:
                messages.info(request, 'Username OR Password is incorrect')

    context_data = {}

    return render(request, "accounts/login.html", context_data)

# View for Register Page
def register_page(request):
    context_data = {}
    return render(request, "accounts/register.html", context_data)

# View for Logout Page
def logout_page(request):
    logout(request)
    return redirect('loginPage')
    
# View for Logout
def logut_page(request):
    data = ''
    return redirect('loginPage')

# View for List all Items
def item_list(request):
    data = ''
    return redirect('loginPage')

# View for Detail an Items
def item_detail(request):
    data = ''
    return redirect('loginPage')
    
# View for Create an Items
def item_create(request):
    data = ''
    return redirect('loginPage')

# View for Update an Items
def item_update(request):

    return redirect('loginPage')

# View for Delete an Items
def item_delete(request):
    data = ''
    return redirect('loginPage')