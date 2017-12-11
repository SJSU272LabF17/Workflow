from __future__ import unicode_literals
from django.db import models
import bcrypt


class UserManager(models.Manager):

    def login(self, postData):
        errors = []
        if User.objects.filter(username=postData['username']):
            db_pw = User.objects.get(username=postData['username']).pw.encode()
            form_pw = postData['pw'].encode('utf8')
            if not bcrypt.checkpw(form_pw, db_pw):
                errors.append('Password is incorret!')
                return [False, errors]
            else:
                user = User.objects.get(username=postData['username'])
                return [True, user]
        else:
            errors.append('User does not exist!')
            return [False, errors]

    def register(self, postData):
        errors = []
        # if len(postData['name']) < 3 :
        #     errors.append('Name should be at least three characters long!')
        # if len(postData['username']) < 3:
        #     errors.append('Userame should be at least three characters long!')
        # if len(postData['pw']) < 8:
        #     errors.append('Passord should be at least 8 characters long!')
        if User.objects.filter(username=postData['username']).first() != None:
            errors.append('Username is already registered!')
        if errors != []:
            return [False, errors]
        else:
            user = User.objects.create(username=postData['username'], name=postData['name'],
                                    pw=bcrypt.hashpw(postData['pw'].encode('utf8'), bcrypt.gensalt()))
        return [True, user]


# class ContainerManager(models.Manager):
#     def validate(self, postData, user_id):
#         errors = []
#         if len(postData['title']) < 1:
#             errors.append('Title can not be empty!')
#             return [False, errors]
#         this_user = User.objects.filter(id=user_id).first()
#         new_container = Container.objects.create(title=postData['title'], author=this_user)
#         print (new_container, "is created")
#         return [True, errors]


class User(models.Model):
    name = models.CharField(max_length=38)
    username = models.CharField(max_length=38)
    pw = models.CharField(max_length=38)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

    class Meta:
        db_table = 'user'

# created checklist
class Container(models.Model):
    author = models.ForeignKey(User, related_name="created_containers", default="")
    title = models.CharField(max_length=38)
    template = models.CharField(max_length=50)
    due_date = models.DateTimeField()
    # objects = ContainerManager()

# section selected
class Checklist(models.Model): 
    container = models.ForeignKey(Container, related_name="contained_lists")
    number =  models.IntegerField(default=0)
    due_date = models.DateTimeField()
    status = models.CharField(max_length=38)
    updated_at = models.DateTimeField(auto_now=True)
    holder = models.ForeignKey(User, related_name="taked_lists", default=None, null=True)

class Field(models.Model):
    checklist = models.ForeignKey(Checklist, related_name="checklist_id")
    field = models.TextField()
    content = models.TextField()

class Item(models.Model):
    name = models.CharField(max_length=38)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # objects = ItemManager()
    author = models.ForeignKey(User, related_name="created_items")
    wished_users = models.ManyToManyField(User, related_name="wished_items")
