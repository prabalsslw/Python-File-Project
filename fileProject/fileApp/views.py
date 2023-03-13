import os
from pyexpat.errors import messages
from django.shortcuts import redirect, render
from .models import *

def home(request):
    alldata = Profile.objects.all()

    return render(request, "Home.html", {"profiles": alldata})

def createUser(request):
    if request.method == 'POST':
        if request.POST['fullname'] and request.POST['email'] and request.POST['phone'] and request.POST['gender']:
           
            fullname = request.POST['fullname']
            email = request.POST['email']
            phone = request.POST['phone']
            gender = request.POST['gender']
            if request.POST['about'] : 
                about = request.POST['about']
            else:
                about = ''

            if request.FILES.get('propic'):
                propic = request.FILES['propic']
            else:
                propic = 'Profilepic/defaultavater.png'

            profile = Profile()
            profile.fullname = fullname
            profile.email = email
            profile.phone = phone
            profile.email = email
            profile.gender = gender
            profile.about = about
            profile.propic = propic
            profile.save()
            # messages.success(request, 'Profile created successfully')
        else:
            messages.error(request, 'Error!')
    else:
        messages.error(request, 'Method not allowed!')
    return redirect('/')


def deleteProfile(request, id):
    profileid = Profile.objects.get(id=id)
    msg = profileid.delete()
    print(msg)
    return redirect(home)

def updateProfile(request):
    if request.method == 'POST':
        if request.POST['pid'] and request.POST['fullname'] and request.POST['email'] and request.POST['phone'] and request.POST['gender']:
            
            pid = request.POST['pid']
            profileid = Profile.objects.get(id=pid)

            fullname = request.POST['fullname']
            email = request.POST['email']
            phone = request.POST['phone']
            gender = request.POST['gender'] 
            about = request.POST['about']

            if request.FILES.get('propic'):
                propic = request.FILES['propic']
                if os.path.isfile(profileid.propic.path):
                    os.remove(profileid.propic.path)
            else:
                propic = profileid.propic
                
            profileid.fullname = fullname
            profileid.email = email
            profileid.phone = phone
            profileid.email = email
            profileid.gender = gender
            profileid.about = about
            profileid.propic = propic
            profileid.save()
            # messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request, 'Error!')
    else:
        messages.error(request, 'Method not allowed!')
    return redirect('/')
