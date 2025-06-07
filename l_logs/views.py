from django.shortcuts import render

# Create your views here.

def index(request):
    """App main page"""
    return render(request, 'l_logs/index.html'
    '')