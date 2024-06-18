from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"index.html")

def contact_us(request):
    return render(request,"contact_us.html")

def login_Reg(request):
    return render(request,"login_Reg.html")