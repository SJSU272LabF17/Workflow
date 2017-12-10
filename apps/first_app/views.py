from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User, Container, Checklist, Field, Item

def home(request):
    # try:
    this_user = User.objects.filter(id=request.session['user_id']).first()
    context = {
    'user': this_user,
    'items': Item.objects.all()
    }
    print (context, "is opening homepage")
    # except:
    #     context = {}
    # print ("find the user is", User.objects.filter(id=request.session['user_id']).first())
    # print ("userid is", request.session['user_id'])
    # print (context, "is opening homepage")
    return render(request, 'first_app/home.html', context)

def register(request):
    print ("register run!")
    postData = {
    'username': request.POST.get('emailsign2', "default email"),
    'name': request.POST.get('name', "default name"),
    'pw': request.POST.get('password', 'default pw'),
    }
    print (postData)
    result = User.objects.register(postData)
    if result[0] == False:
        for error in result[1]:
            messages.error(request, error)
        return redirect('/signin')
    else:
        request.session['user_id'] = result[1].id
    return redirect('/') 

def login(request):
    postData = {
    'username': request.POST.get('emailsign1', "default email"),
    'pw': request.POST.get('pw', 'default pw'),
    }
    result = User.objects.login(postData)
    if result[0] == False:
        for error in result[1]:
            messages.error(request, error)
        return redirect('/signin')
    else:
       
        request.session['user_id'] = result[1].id
        print (request.session['user_id'], "is logged in")
        return redirect('/')

def logout(request):
    request.session['user_id'] = None
    return redirect('/signin')

def create_new(request):
    this_user = User.objects.filter(id=request.session['user_id']).first()
    title = request.POST.get('title', False)
    date = request.POST.get('date', False)
    temp = request.POST.get('temp', False)
    postData = {
    'title': title,
    'date': date,
    'temp': temp
    }
    newContainer = Container.objects.create(title=postData['title'], due_date=postData['date'], author=this_user, template=postData['temp'])
    # result = Container.objects.validate(postData, request.session['user_id'])
    # if result[0] == False:
    #     for error in result[1]:
    #         messages.error(request, error)
    #     return redirect('create_new')
    # else:
        # return redirect('/createSuccess') 
    print ("db result is adding", newContainer)
    return redirect('/createSuccess')

def createSuccess(request):
    try:
        this_user = User.objects.filter(id=request.session['user_id']).first()
        context = {
        'user': this_user,
        'items': Item.objects.all()
        }
        print (context, "is opening homepage")
    except:
        context = {}
    return render(request, 'first_app/createSuccess.html', context)
# def item(request, item_id):
#     item = Item.objects.filter(id=item_id).first()
#     context = {
#     'item': item
#     }
#     return render(request, 'first_app/item.html', context)

# def add_wish(request, item_id):
#     this_user = User.objects.filter(id=request.session['user_id']).first()
#     this_item = Item.objects.filter(id=item_id).first()
#     this_item.wished_users.add(this_user)
#     return redirect('/dashboard')

# def remove_wish(request, item_id):
#     this_user = User.objects.filter(id=request.session['user_id']).first()
#     this_item = Item.objects.filter(id=item_id).first()
#     this_item.wished_users.remove(this_user)
#     return redirect('/dashboard')

# def delete_item(request, item_id):
#     Item.objects.filter(id=item_id).first().delete()
#     return redirect('/dashboard')

def chngPswd(request):
    try:
        this_user = User.objects.filter(id=request.session['user_id']).first()
        context = {
        'user': this_user,
        'items': Item.objects.all()
        }
        print (context, "is opening homepage")
    except:
        context = {}
    return render(request, 'first_app/chngPswd.html', context)

def contact(request):
    try:
        this_user = User.objects.filter(id=request.session['user_id']).first()
        context = {
        'user': this_user,
        'items': Item.objects.all()
        }
        print (context, "is opening homepage")
    except:
        context = {}
    return render(request, 'first_app/contact.html', context)

def contributors(request):
    try:
        this_user = User.objects.filter(id=request.session['user_id']).first()
        context = {
        'user': this_user,
        'items': Item.objects.all()
        }
        print (context, "is opening homepage")
    except:
        context = {}
    return render(request, 'first_app/contributors.html', context)

def project(request):
    try:
        this_user = User.objects.filter(id=request.session['user_id']).first()
        context = {
        'user': this_user,
        'items': Item.objects.all()
        }
        print (context, "is opening homepage")
    except:
        context = {}
    return render(request, 'first_app/project.html', context)

def sampleChecklist(request):
    try:
        this_user = User.objects.filter(id=request.session['user_id']).first()
        context = {
        'user': this_user,
        'items': Item.objects.all()
        }
        print (context, "is opening homepage")
    except:
        context = {}
    return render(request, 'first_app/sampleChecklist.html', context)

def savedChecklist(request):
    try:
        this_user = User.objects.filter(id=request.session['user_id']).first()
        context = {
        'user': this_user,
        'items': Item.objects.all()
        }
        print (context, "is opening homepage")
    except:
        context = {}
    return render(request, 'first_app/savedChecklist.html', context)

def about(request):
    try:
        this_user = User.objects.filter(id=request.session['user_id']).first()
        context = {
        'user': this_user,
        'items': Item.objects.all()
        }
        print (context, "is opening homepage")
    except:
        context = {}
    return render(request, 'first_app/about.html', context)

def services(request):
    try:
        this_user = User.objects.filter(id=request.session['user_id']).first()
        context = {
        'user': this_user,
        'items': Item.objects.all()
        }
        print (context, "is opening homepage")
    except:
        context = {}
    return render(request, 'first_app/services.html', context)

def signin(request):
    try:
        this_user = User.objects.filter(id=request.session['user_id']).first()
        context = {
        'user': this_user,
        'items': Item.objects.all()
        }
        print (context, "is opening homepage")
    except:
        context = {}
    return render(request, 'first_app/signin.html', context)

def contact(request):
    try:
        this_user = User.objects.filter(id=request.session['user_id']).first()
        context = {
        'user': this_user,
        'items': Item.objects.all()
        }
        print (context, "is opening homepage")
    except:
        context = {}
    return render(request, 'first_app/Contact.html', context)

def newchecklist(request):
    try:
        this_user = User.objects.filter(id=request.session['user_id']).first()
        context = {
        'user': this_user,
        'items': Item.objects.all()
        }
        print (context, "is opening homepage")
    except:
        context = {}
    return render(request, 'first_app/newchecklist.html', context)

def dashBoard(request):
    try:
        this_user = User.objects.filter(id=request.session['user_id']).first()
        context = {
        'user': this_user,
        'items': Item.objects.all()
        }
        print (context, "is opening homepage")
    except:
        context = {}
    return render(request, 'first_app/dashBoard.html', context)

def checklist(request):
    try:
        this_user = User.objects.filter(id=request.session['user_id']).first()
        context = {
        'user': this_user,
        'items': Item.objects.all()
        }
        print (context, "is opening homepage")
    except:
        context = {}
    return render(request, 'first_app/checklist.html', context)

def showTemplates(request):
    try:
        this_user = User.objects.filter(id=request.session['user_id']).first()
        context = {
        'user': this_user,
        'items': Item.objects.all()
        }
        print (context, "is opening homepage")
    except:
        context = {}
    return render(request, 'first_app/templates.html', context)

def savedChecklists(request):
    try:
        this_user = User.objects.filter(id=request.session['user_id']).first()
        context = {
        'user': this_user,
        'items': Item.objects.all()
        }
        print (context, "is opening homepage")
    except:
        context = {}
    return render(request, 'first_app/savedChecklists.html', context)

def itmain(request):
    try:
        this_user = User.objects.filter(id=request.session['user_id']).first()
        context = {
        'user': this_user,
        'items': Item.objects.all()
        }
        print (context, "is opening homepage")
    except:
        context = {}
    return render(request, 'first_app/itmain.html', context)

def coffeemain(request):
    try:
        this_user = User.objects.filter(id=request.session['user_id']).first()
        context = {
        'user': this_user,
        'items': Item.objects.all()
        }
        print (context, "is opening homepage")
    except:
        context = {}
    return render(request, 'first_app/coffeemain.html', context)

def constructmain(request):
    try:
        this_user = User.objects.filter(id=request.session['user_id']).first()
        context = {
        'user': this_user,
        'items': Item.objects.all()
        }
        print (context, "is opening homepage")
    except:
        context = {}
    return render(request, 'first_app/constructmain.html', context)

