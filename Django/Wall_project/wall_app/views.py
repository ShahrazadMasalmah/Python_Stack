from email import message
from django.shortcuts import render, redirect
from login_app.models import *
import random

def index(request):
   user_id = request.session['user_id']
   get_user = User.objects.get(id = user_id)
   context = {
      "this_user" : get_user,
      "users" : User.objects.all()
   }
   return render(request, "wall.html", context)

def addMessage(request):
   user_id = request.session['user_id']
   user = User.objects.get(id = user_id)
   message = request.POST['message']
   this_message = Message.objects.create(message = message, user = user)
   request.session['message'] = this_message.id
   return redirect("/wall")

def addComment(request):
   users = User.objects.all()
   random_number = random.randrange(0,len(users))
   print(random_number)
   for i in range(len(users)):
      if random_number == i:
         this_user = User.objects.get(id = users[i].id)

   this_message = Message.objects.get(id = request.POST['message_id'])
   comment = request.POST['comment']
   this_comment = Comment.objects.create(comment = comment, message = this_message, user = this_user)
   return redirect("/wall")

def deleteMessage(request):
   this_message = Message.objects.get(id = request.POST['message_id'])
   this_message.delete()
   return redirect("/wall")

def logout(request):
   request.session.flush()
   return redirect("/")