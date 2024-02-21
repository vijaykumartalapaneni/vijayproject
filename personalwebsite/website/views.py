from django.shortcuts import render

# Create your views here.
def homeview(request):
    return render(request,'home.html')
def workview(request):
    return render(request,'work.html')
def projectview(request):
    return render(request,'projects.html')
def contactview(request):
    return render(request,'contact.html')
def educationview(request):
    return render(request,'education.html')

