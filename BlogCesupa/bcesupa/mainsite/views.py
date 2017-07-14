from django.shortcuts import render

def homepage(request):
	return render(request, 'html/homepage.html')

def contactPage(request):
	return render(request, 'html/contactpage.html')