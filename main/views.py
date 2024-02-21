from django.shortcuts import render

# Create your views here.
def main(request):
    return render(request,'main/main.html')

def about(request):
    return render(request,'main/about.html')

def services(request):
    return render(request,'main/services.html')
def base(request):
    return render(request,'main/base.html')