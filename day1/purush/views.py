from django.shortcuts import render
from django.http import HttpResponse
 
def a(rq):
	return HttpResponse("hi purushotham")
def b(rq, nam,ag):
	return HttpResponse("nam:{}</br>ag:{}".format(nam,ag))
def home(rq):
	return HttpResponse("<h2 style='background-color:blue'>welcome <span style='color:blue'>to</span> home page</h2>")

def chk(rq):
	return HttpResponse("<script>alert('hi this is purushotham')</script><h2>purushotham</h2>")


def homepage(rq):
	return render(rq,'ht/home.html')
def login(rq):
	return render(rq,'ht/login.html')
def reg(rq):
	return render(rq,'ht/register.html')