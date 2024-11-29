# customers/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import ServiceRequest
from .forms import ServiceRequestForm

def landing_page(request):
    return render(request, 'customers/landing_page.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

@login_required
def request_service(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST, request.FILES)
        if form.is_valid():
            service_request = form.save(commit=False)
            service_request.customer = request.user
            service_request.save()
            return redirect('track_request')
    else:
        form = ServiceRequestForm()
    return render(request, 'customers/request_service.html', {'form': form})

@login_required
def track_request(request):
    requests = ServiceRequest.objects.filter(customer=request.user)
    return render(request, 'customers/track_request.html', {'requests': requests})

@login_required
def account_info(request):
    return render(request, 'customers/account_info.html', {'user': request.user})