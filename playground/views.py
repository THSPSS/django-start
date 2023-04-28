from django.shortcuts import render
from django.http import HttpResponse

def calculate() :
    x = 1
    y = 2
    return x

def say_hello(request) :
    x = calculate()
    return render(request , 'hello.html',{'name' : 'Guest'})


# Create your views here.
# request handler
# request -> response
# action 
# run without debugging