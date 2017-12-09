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


class ItemManager(models.Manager):
    def validate(self, postData, user_id):
        errors = []
        if len(postData['name']) < 1:
            errors.append('Item can not be empty!')
            return [False, errors]
        if len(postData['name']) < 3:
            errors.append('Item name should be more than three charaters long!')
            return [False, errors]
        this_user = User.objects.filter(id=user_id).first()
        new_item = Item.objects.create(name=postData['name'], author=this_user)
        new_item.wished_users.add(this_user)
        return [True, errors]


class User(models.Model):
    name = models.CharField(max_length=38)
    username = models.CharField(max_length=38)
    pw = models.CharField(max_length=38)
    # h_date = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # objects = UserManager()

    class Meta:
        db_table = 'user'


class Container(models.Model):
    user = models.ForeignKey(User, related_name="user_id")
    title = models.CharField(max_length=38)
    template = models.CharField(max_length=50)
    due_date = models.DateTimeField()


class Checklist(models.Model):
    container = models.ForeignKey(Container, related_name="container_id")
    name = models.CharField(max_length=50)
    due_date = models.DateField()
    status = models.CharField(max_length=38)
    updated_at = models.DateTimeField(auto_now=True)


class Field(models.Model):
    checklist = models.ForeignKey(Checklist, related_name="checklist_id")
    field = models.TextField()
    content = models.TextField()


class Item(models.Model):
    name = models.CharField(max_length=38)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ItemManager()
    author = models.ForeignKey(User, related_name="created_items")
    wished_users = models.ManyToManyField(User, related_name="wished_items")
