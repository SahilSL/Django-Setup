from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')
    #return HttpResponse("<h1>Hogya Bhai Ab aage ka Hard hai</h1>")

def about(request):
    return HttpResponse("<h1>Le Bhai About bhi bana diya</h1>")

def services(request):
    return HttpResponse("<h1>Le Bhai Services bhi bana diya</h1>")

def contact(request):
    return HttpResponse("<h1>Le Bhai contact bhi bana diya</h1>")