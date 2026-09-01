from django.shortcuts import render

# Create your views here.

def home(request):
    items = [
        {'name': 'Computer Hardware Repair', 'completed': True},
        {'name': 'Software Skills', 'completed': True},
        {'name': 'Basic Coding Skills', 'completed': True},
        {'name': 'Advanced Coding Skills', 'completed': False},
        {'name': 'Complete CIDM 3312', 'completed': False},
    ]
    context = {'items': items}
    return render(request, 'pages/home.html', context)

def about(request):
    return render(request, 'pages/about.html')

def contact(request):
    return render(request, 'pages/contact.html')