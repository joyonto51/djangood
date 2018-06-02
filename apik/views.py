from django.shortcuts import render,HttpResponse

def index(request):
    return HttpResponse("Hello, Jayanta. You are in apik index.")