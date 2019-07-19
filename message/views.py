from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

def home(request):
	messages = {
		'messages': Post.objects.all()
	}
	return render(request, 'apotofgold/home.html', messages)

def about(request):
	return render(request, 'apotofgold/about.html',{'title':'About'})	

