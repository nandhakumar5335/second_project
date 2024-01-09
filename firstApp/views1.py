from django.shortcuts import render
from django.http import HttpResponse

def wish(request):
	message ='<h1>Hi buddy how are you</h>'
	return HttpResponse(message)
# Create your views here.
def gm_view(request):
	return HttpResponse('<h1> Good Morning</h1>')
def ga_view(request):
	return HttpResponse('<h1> Good afternoon</h1>')
def ge_view(request):
	return HttpResponse('<h1> Good evening</h1>')