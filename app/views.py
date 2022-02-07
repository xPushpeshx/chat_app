from django.shortcuts import render

# Create your views here.
def index(request,gpname):
    return render(request,'index.html',{'gpname':gpname})