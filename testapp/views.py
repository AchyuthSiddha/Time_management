from django.shortcuts import render
import datetime
# Create your views here.
def Wish(request):
    time=datetime.datetime.now()
    msg='Hello friends very'
    h=int(time.strftime('%H'))
    if h<12:
        msg+='Good morning'
    elif h<16:
        msg+="good afternoon"
    elif h<21:
        msg+='Good night'
    d={'time':time,'name':'Achyuth','age':28,'loc':'hyd','insert_msg':msg}
    return render(request,'testapp/time.html',d)