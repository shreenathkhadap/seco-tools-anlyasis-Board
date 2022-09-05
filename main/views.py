from asyncio.windows_events import NULL
from queue import Empty
from django import contrib
from django.shortcuts import redirect, render, HttpResponse
from datetime import datetime
from firebase import firebase
from requests import post, get
from firebase.firebase import FirebaseApplication, FirebaseAuthentication
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth import SESSION_KEY, authenticate
from django.contrib.auth import logout, login
import pyrebase
from pyrebase.pyrebase import Database
import firebase_admin
from firebase_admin import credentials


# database connection
config = {
    "apiKey": "AIzaSyCudRjL427kpFI2zH4JzXkfZ9p0E2eK0tw",
    "authDomain": "sktrail-c3fea.firebaseapp.com",
    "databaseURL": "https://sktrail-c3fea-default-rtdb.firebaseio.com",
    "projectId": "sktrail-c3fea",
    "storageBucket": "sktrail-c3fea.appspot.com",
    "messagingSenderId": "938378843204",
    "appId": "1:938378843204:web:566ad8ef9c789a28f61811",
    "measurementId": "G-HSD9BXJ91S"
}

firebase = pyrebase.initialize_app(config)
authe = firebase.auth()
database = firebase.database()
cred = credentials.Certificate(
    'sktrail-c3fea-firebase-adminsdk-attkx-0198865b65.json')
firebase_admin.initialize_app(cred)
import datetime


def index(request):
    currentdate = datetime.date.today()
    formatDate = currentdate.strftime("%d/%b/%y")
    return render(request,'home.html',{'current_date':currentdate,'format_date':formatDate} )  

def main_admin(request):
    return render(request,'login.html' ) 

def login(request):
    pass1 = request.POST.get('psw')
    oldcopq=20
    pass2="51151213"


    if pass1==pass2:
        print(pass1)
        print(pass2)
        return render(request,'main_admin.html',{'oldcopq':oldcopq} )
    else:
        msg="Wrong Password"
        print("from else",pass1)
        print(pass2)
        return render(request,'login.html',{'msg':msg} )


def getdata(request):
    
    Tcopq = request.POST.get('tcopq')
    Newcopq = request.POST.get('newcopq')
    print("fetched T :--",Tcopq)
    print("fetched N :--",Newcopq)
    
    
    
    Tpr = request.POST.get('tpr')
    Newpr= request.POST.get('newpr')
    
    
    Tmo = request.POST.get('tmo')
    Newmo = request.POST.get('newmo')
    
    
    Tyeild = request.POST.get('tYeild')
    Newyeild = request.POST.get('newYeild')

    if Newcopq=="" :
        
        print('Var null',Newcopq)

    else:
        print("im not null",Newcopq)    
    # if Tcopq==Empty :
        
    #     print('Var null',Tcopq)

    # else:
    #     print("im not null",Tcopq)    
    
    
    
        # print("im run")
        
        
        
    return render(request,'main_admin.html' ) 
    






    


#     database.child("Data").child("Events").push(data)

#     msg = "successfully registered Event!"
#     return render(request, 'index.html', {"msg": msg})
