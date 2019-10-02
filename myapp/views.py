from django.shortcuts import render

# Create your views here.
def page1(request):
    
    return render(request,'sample1.html',context={'data':"Raju"})

def page2(request):
    d={'info':"DJANGO class"}
    return render(request,'sample2.html',context=d)
    
def page3(request):
    return render(request,'sample3.html')
    