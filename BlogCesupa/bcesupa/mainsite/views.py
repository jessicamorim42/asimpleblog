from django.shortcuts import render

def homepage(request):
	return render(request, 'html/homepage.html')

def contactpage(request):
	return render(request, 'html/contactpage.html')

def newspage(request):
	return render(request, 'html/newspage.html')

def projectspage(request):
	return render(request, 'html/projectspage.html')

