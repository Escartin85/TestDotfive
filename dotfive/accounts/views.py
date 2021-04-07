from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse, HttpResponseRedirect, Http404

from .models import Item
from .forms import ItemForm, CreateNewUserForm

# Create your views here.
# View for Home Page
def home_page(request):
    # return render(request, "index.html", context_data)
    return redirect('loginPage')

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
    

# View for List all Items
def item_list(request):
    # request all the Item objects
    queryset_list_items = Item.items.all()
  
    # parse the query into context data
    context_data = {
        "Title": "List of all Items",
		"items_list": queryset_list_items,
    }
    
    # render the view
    return render(request, "accounts/item_list.html", context_data)

# View for Detail an Items
def item_detail(request, slug=None):

    # check if the User is NOT registered or is NOT a SuperUser
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404

    # get an object's instance
    instance = get_object_or_404(Item, slug=slug)

    # parse the query into context data
    title = "Detail of: " + slug

    # parse the query into context data
    context_data = {
        "Title": title,
        "item": instance,
    }
    return render(request, "accounts/item_detail.html", context_data)
    
# View for Create an Items
def item_create(request):
    
    # check if the User is NOT registered or is NOT a SuperUser
    if not request.user.is_staff or not request.user.is_superuser:
        return Http404

    # create the form for by Item Form
    itemForm = ItemForm(request.POST or None)

    # validate the data input on the form
    if itemForm.is_valid():
        # save the data after been validated
        instance = itemForm.save(commit=False)
        instance.save()
        
        # Message success
        messages.success(request, "New Item Created")
        return HttpResponseRedirect(instance.get_absolute_url())
    
    # parse the query into context data
    context_data = {
        "itemForm": itemForm,
        "mode": "create",
    }

    return render(request, "accounts/item_form.html", context_data)

# View for Update an Items
def item_update(request, slug=None):

    # check if the User is NOT registered or is NOT a SuperUser
    if not request.user.is_staff or not request.user.is_superuser:
        return Http404

    # get an object's instance
    instance = get_object_or_404(Item, slug=slug)
    # create the form for by Item Form
    itemForm = ItemForm(request.POST or None)

    # validate the data input on the form
    if itemForm.is_valid():
        # save the data after been validated
        instance = itemForm.save(commit=False)
        instance.save()
        
        # Message success
        messages.success(request, "Item Updated")
        return HttpResponseRedirect(instance.get_absolute_url())
    else:
        if not instance:
            messages.error(request, "Couldn't updated the Item")
    
    # parse the query into context data
    context_data = {
        "itemForm": itemForm,
        "mode": "create",
        'instance': instance,
    }

    return render(request, "accounts/item_form.html", context_data)

# View for Delete an Items
def item_delete(request, slug=None):
    # check if the User is NOT registered or is NOT a SuperUser
    if not request.user.is_staff or not request.user.is_superuser:
        return Http404

    # get an object's instance
    instance = get_object_or_404(Item, slug=slug)
    # delete data from table
    instance.delete()
    # Message success
    messages.success(request, "Item Added successful")
    return redirect('loginPage')