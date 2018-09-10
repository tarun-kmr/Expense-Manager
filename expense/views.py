from django.shortcuts import render
from django.contrib.auth import logout

def logout(request):
    logout(request)
    return render(request, 'expense/index.html')

def index(request):
    return render(request, 'expense/index.html')

