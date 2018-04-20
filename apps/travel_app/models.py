from __future__ import unicode_literals
from django.db import models
import datetime

class UserManager(models.Manager):

    def validate_Registration(self, postData):
        errors = {}
        u = User.objects.filter(username = postData['username'])

        if(u != None and len(u) > 0):
            errors["account"] = "Account already exists!"
        elif len(postData['name']) < 3 or len(postData['username']) < 3:
            errors["names"] = "Name or Username may not be less than 3 characters!"
        elif len(postData['password']) < 8:
            errors["password"] = "Invalid password!"
        elif postData['password'] != postData['confirmpassword']:
            errors["password"] = "Passwords don't match!"
        return errors

    def Validate_Login(self, postData):
        errors = {}
        u = User.objects.filter(username = postData['login_username'], password = postData['login_password'])
        if u == None:
            errors["email"] = "User account does not exist!"
        elif len(User.objects.filter(username = postData['login_username'])) < 1:
            errors["email"] = "User account does not exist!"
        elif len(User.objects.filter(password = postData['login_password'])) < 1:
            errors["password"] = "Invalid password!"

        print(u)
        return errors
            

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=28)
    password = models.CharField(max_length=55)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()
    def __repr__(self):
        return "<User object: '{}', '{}', '{}'>".format(self.name, self.username,self.created_at)

class TravelPlan_Manager(models.Manager):

    def validate(self, postData):
        errors = {}
        date_from = datetime.datetime.strptime('{}'.format(postData['date_from']) , '%Y-%m-%d')
        date_to = datetime.datetime.strptime('{}'.format(postData['date_to']) , '%Y-%m-%d')

        if len(postData['destination']) < 1 or len(postData['description']) < 1 or len(postData['date_to']) < 1 or len(postData['date_from']) < 1:
            errors["Fields"] = "All Fields must be filled out!"
        elif date_from.date() < datetime.datetime.now().date() or date_to.date() <= datetime.datetime.now().date():
            errors["dates"] = "Travel dates must be in the future"
        elif date_to.date() <= date_from.date():
            errors["dates"] = "Travel date to must be in the future!"
        return errors


class TravelPlan(models.Model):
    destination = models.CharField(max_length=255)
    description = models.TextField()
    date_from = models.DateTimeField()
    date_to = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    owner = models.ForeignKey(User, related_name = 'created_trips', on_delete=models.PROTECT, null=True)
    users = models.ManyToManyField(User, related_name = 'trips')
    objects = TravelPlan_Manager()
    def __repr__(self):
        return "<User object: '{}', '{}', '{}', '{}'>".format(self.destination, self.description ,self.date_from, self.date_to)
