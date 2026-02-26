from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, "home.html")

def submit(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    if username == "admin" and password == "admin":
        print("Tumpak")
    else:
        return render(request, "home.html")