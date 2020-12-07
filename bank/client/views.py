from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserForm


def index(request):
    userform = UserForm()
    if request.method == "POST":
        userform = UserForm(request.POST)
        if userform.is_valid():
            Pib = userform.cleaned_data["Pib"]
            return HttpResponse("<h1>Здравстуйте: {0}, картка оформлена</h1>".format(Pib))
    return render(request, "index.html", {"form": userform})