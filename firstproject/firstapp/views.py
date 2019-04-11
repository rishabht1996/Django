from django.shortcuts import render
from django.http import HttpResponse
from firstapp import forms

# Create your views here.

def index(request):
    return HttpResponse("Hello, I just created My First Application.")

def rishabh(request):
    return HttpResponse("Hello I ma the second Function")

def example(request):
    return HttpResponse("Hello I am an example")


def template_demo(request):
    dict_var= {'random_var':" I am Written in Views.py"}
    return render(request,'firstapp/index.html', context= dict_var)


def form_view(request):
    form=forms.FormName()
    if request.method == "POST":
        form = forms.FormName(request.POST)
        form.save()

    return render(request,'firstapp/basic_form.html',{'form':form})



