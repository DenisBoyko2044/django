from django.shortcuts import render
 
def index(request):
    return render(request, "index.html")
def ENartistic(request):
    return render(request, "ENartistic.html")
def ENstrict(request):
    return render(request, "ENstrict.html")
def UAartistic(request):
    return render(request, "UAartistic.html")
def UAstrict(request):
    return render(request, "UAstrict.html")