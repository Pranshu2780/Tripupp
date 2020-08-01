from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def main(request):
    context={}
    return render(request,'demo/main.html',context)


def exams(request):
    context={}
    return render(request,'demo/exams.html',context)
  
  
def jeemains(request):
    context={}
    return render(request,'demo/jeemains.html',context)
   
def jeeadvanced(request):
    context={}
    return render(request,'demo/jeeadvanced.html',context)
  
def pdf(request):
    context={}
    return render(request,'demo/pdf.html',context)

def tenth(request):
    context={}
    return render(request,'demo/tenth.html',context)

def twelveth(request):
    context={}
    return render(request,'demo/twelveth.html',context)
