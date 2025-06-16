from django.shortcuts import render, redirect

def home(request):
    return render(request, 'index.html')
def about(request):
    return render(request, 'about.html')
def contact(request):
    return render(request, 'contact.html')
def new(request):
    return render(request, 'new.html')
def popular(request):
    return render(request, 'popular.html')
def search(request):
    return render(request, 'search.html')
def sign_in(request):
    return render(request, 'signin.html')
def addMovies(request):
    return render(request, 'addMovies.html')