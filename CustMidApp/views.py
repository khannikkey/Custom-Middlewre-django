from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    print("This line Printing at View Function")
    return HttpResponse ("<h1>Hi Nikkey....... Welcome To Django World </h1>")