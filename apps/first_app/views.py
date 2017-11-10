from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User, Item

def index(request):
    context = {
    'users' : User.objects.all()
    }
    return render(request, 'first_app/index.html', context)

def register(request):
    if request.POST['pw'] != request.POST['c_pw']:
        messages.error(request, "Passwords does not match")
        return redirect('/main') 
    postData = {
    'name': request.POST['name'],
    'username': request.POST['username'],
    'h_date': request.POST['h_date'],
    'pw': request.POST['pw'],
    }
    result = User.objects.register(postData)
    if result[0] == False:
        for error in result[1]:
            messages.error(request, error)
        return redirect('/main')
    else:
        request.session['user_id'] = result[1].id
        return redirect('/dashboard') 

def login(request):
    postData = {
    'username': request.POST['username'],
    'pw': request.POST['pw'],
    }
    result = User.objects.login(postData)
    if result[0] == False:
        for error in result[1]:
            messages.error(request, error)
        return redirect('/main')
    else:
        request.session['user_id'] = result[1].id
        return redirect('/dashboard')

def logout(request):
    request.session['user_id'] = None
    return redirect('/main')

# def dashboard_1(request):
#     this_user = User.objects.filter(id=request.session['user_id']).first()
#     context = {
#     'user': this_user,
#     'items': Item.objects.all()
#     }
#     return render(request, 'first_app/dashboard_1.html', context)

def dashboard(request):
    this_user = User.objects.filter(id=request.session['user_id']).first()
    context = {
    'user': this_user,
    'items': Item.objects.all()
    }
    return render(request, 'first_app/dashboard.html', context)

def create_new(request):
    return render(request, 'first_app/newChecklist.html')

def create_process(request):
    name = request.POST.get('name', False)
    # print name
    postData = {
    'name': name,
    }
    result = Item.objects.validate(postData, request.session['user_id'])
    if result[0] == False:
        for error in result[1]:
            messages.error(request, error)
        return redirect('/wish_items/create')
    else:
        return redirect('/dashboard') 

def item(request, item_id):
    item = Item.objects.filter(id=item_id).first()
    context = {
    'item': item
    }
    return render(request, 'first_app/item.html', context)

def add_wish(request, item_id):
    this_user = User.objects.filter(id=request.session['user_id']).first()
    this_item = Item.objects.filter(id=item_id).first()
    this_item.wished_users.add(this_user)
    return redirect('/dashboard')

def remove_wish(request, item_id):
    this_user = User.objects.filter(id=request.session['user_id']).first()
    this_item = Item.objects.filter(id=item_id).first()
    this_item.wished_users.remove(this_user)
    return redirect('/dashboard')

def delete_item(request, item_id):
    Item.objects.filter(id=item_id).first().delete()
    return redirect('/dashboard')
