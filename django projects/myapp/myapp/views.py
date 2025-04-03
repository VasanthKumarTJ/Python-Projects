from django.shortcuts import render, redirect

def custom_404(request, exception):
    return render(request, '404.html', status=404)