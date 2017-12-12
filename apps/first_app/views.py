from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User, Container, Checklist, Field, Item
import json

def test(request):
    return render(request, 'first_app/test.html')
def test_new(request):
    print (request.POST.get('interest'))
    return redirect('/test')

def home(request):
    try:
        this_user = User.objects.filter(id=request.session['user_id']).first()
        context = {
        'user': this_user,
        'items': Item.objects.all()
        }
        # print (context, "is opening homepage")
    except:
        context = {}
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
    sections = request.POST.getlist('sections', False)
    # print ("sections are", sections)
    postData = {
    'title': title,
    'date': date,
    'temp': temp
    }
    newContainer = Container.objects.create(title=postData['title'], due_date=postData['date'], author=this_user, template=postData['temp'])
    for s in sections:
        newChecklist = Checklist.objects.create(container=newContainer, due_date=postData['date'], number=s)
        # print (newChecklist, "is added")
    # print ("db result is adding", newContainer)
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

def delete(request, container_id):
    Container.objects.filter(id=container_id).first().delete()
    return redirect('/dashBoard')

def show(request, container_id):
    this_container = Container.objects.filter(id=container_id).first()
    this_temp = this_container.template
    lists = Checklist.objects.filter(container=this_container)
    numbers = []
    for s in lists:
        numbers.append(s.number)
    print ("temp is showing", numbers)
    context = {
    'container': this_container,
    'sections': numbers,
    'lists':lists
    }
    print ("lists are", lists)
    if this_temp == "building":
        return render(request, 'first_app/constructmain.html', context)
    elif this_temp == "coffee":
        return render(request, 'first_app/coffeemain.html', context)
    elif this_temp == "it":
        return render(request, 'first_app/itmain.html', context)
    else:
        return render(request, 'first_app/dashboard.html', context)
    
def edit(request, container_id):
    this_user = User.objects.filter(id=request.session['user_id']).first()
    this_container = Container.objects.filter(id=container_id).first()
    this_lists = Checklist.objects.filter(container=this_container)
    this_section_number = request.POST.get('section', False)
    change_status = request.POST.get('status', False)
    change_due_date = request.POST.get('due_date', False)
    Checklist.objects.filter(container=this_container, number=this_section_number).update(status=change_status, due_date=change_due_date, holder=this_user)

    showlink = '/show/' + str(this_container.id)
    return redirect(showlink)

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
        all_checklists = Container.objects.all()
        checklists_with_data = []
        for list in all_checklists:
            checklists_with_data.append(list)
            sections = Checklist.objects.filter(container=list)
            section_titles = ["Construction Planning","Environmental Testing and Surveying","Buying Land","Construction Design","Pre-Construction","Procurement","Construction","Post-Construction"]
            closed = in_progress = completd = locked = 0
            people = {}
            for s in sections:
                s.title = section_titles[s.number - 1]
                ss = s.status
                if ss == "Closed":
                    closed += 1
                elif ss == "Completed":
                    completd += 1
                elif ss == "In Progress":
                    in_progress += 1
                else:
                    locked += 1
                # person = User.objects.create()
                person = s.holder
                print ("person is ", person)
                if person:
                    p = person.name
                    print ("name is ", p)
                    if p in people:
                        people[p] += 1
                    else:
                        people[p] = 0
            list.sections = sections
            total = len(sections)
            # calculate pi graph
        # pie_start1 = 0
        # pie_end1 = completd * 360 / total 
        # pie_start2 = pie_end1
        # pie_end2 = in_progress * 360 / total
        # pie_start3 = pie_start2 + pie_end2
        # pie_end3 = locked * 360 / total
        # pie_start4 = pie_start3 + pie_end3
        # pie_end4 = closed * 360 / total
        # calculate bar
        # progress1 = people.values()[0] * 100 / total
        # progress2 = people.values()[1] * 100 / total
        # progress3 = people.values()[2] * 100 / total
        # progress4 = people.values()[3] * 100 / total
            
        context = {
        'user': this_user,
        'checklists': checklists_with_data,
        'closed': closed,
        'in_progress': in_progress ,
        'completed': completd,
        'locked': locked,
        # 'pie_start1': pie_start1, 'pie_end1': pie_end1, 'pie_start2': pie_start2, 'pie_end2': pie_end2,
        #             'pie_start3':pie_start3, 'pie_end3': pie_end3, 'pie_start4': pie_start4, 'pie_end4': pie_end4,
        # 'user1_progress': progress1 ,  'user1_name': people[0], 
        #             'user2_progress': progress2 , 'user2_name': people.keys()[1], 
        #             'user3_progress': progress3 , 'user3_name': people.keys()[2], 
        #             'user4_progress': progress4 , 'user4_name': people.keys()[3],
        }
    except:
        context = {}
    print (context, "is passed into dashboard")
    return render(request, 'first_app/dashBoard.html', context)

# def data():
    
#     pie_start1 = 0
#     pie_end1 = completed * 360 / total 
#     pie_start2 = pie_end1
#     pie_end2 = in_progress * 360 / total
#     pie_start3 = pie_start2 + pie_end2
#     pie_end3 = locked * 360 / total
#     pie_start4 = pie_start3 + pie_end3
#     pie_end4 = closed * 360 / total
#     user1_progress

#     context ={ 'pie_start1': pie_start1, 'pie_end1': pie_end1, 'pie_start2': pie_start2, 'pie_end2': pie_end2,
#                 'pie_start3':pie_start3, 'pie_end3': pie_end3, 'pie_start4': pie_start4, 'pie_end4': pie_end4,
#                 'user1_progress': 60, 'title1': 'b', 'user1_name': 'user1', 'status1': 'Locked', 'date1': '11/01',
#                 'user2_progress': 40, 'title2': 'b', 'user2_name': 'user2', 'status2': 'Locked', 'date2': '11/01',
#                 'user3_progress': 20, 'title3': 'b', 'user3_name': 'user3', 'status3': 'Locked', 'date3': '11/01',
#                 'user4_progress': 10, 'title4': 'b', 'user4_name': 'user4', 'status4': 'Locked', 'date4': '11/01',
#                 }
#     return render(request, 'first_app/dashBoard.html', context)

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
        'sections': [1,2,3,4,5,6,7,8]
        }
        print (context, "is opening homepage")
    except:
        context = {}
    return render(request, 'first_app/constructmain.html', context)

