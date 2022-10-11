from django.shortcuts import render,HttpResponse

def root(request):
    return HttpResponse('welcome')
