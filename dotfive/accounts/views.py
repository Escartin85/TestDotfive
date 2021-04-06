from django.shortcuts import render, redirect

# Create your views here.
# View for Home Page
def home_page(request):

    data = ''
    context_data = {
        "formWorker": data,
        "Title": "Home",
    }

    #return render(request, "index.html", context_data)
    return redirect('loginPage')

# View for Login Page
def login_page(request):
    data = ''
    context_data = {
        "formWorker": data,
        "Title": "Home",
    }

    return render(request, "accounts/login.html", context_data)

# View for Register Page
def register_page(request):
    data = ''
    return redirect('loginPage')

# View for Logout Page
def logout_page(request):
    data = ''
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