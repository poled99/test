from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, "home.html")

def submit(request):
    if request.method == "POST":
        firstname = request.POST.get('firstname')
        middlename = request.POST.get('middlename')
        lastname = request.POST.get('lastname')
        
        print(f"Firstname: {firstname}")
        print(f"Middlename: {middlename}")
        print(f"Lastname: {lastname}")
        
        # Optional: You can add a success message or redirect
        return render(request, "home.html")
    else:
        # If someone tries to access submit page directly via GET
        return render(request, "home.html")