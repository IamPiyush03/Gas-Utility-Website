from django.shortcuts import render
from customers.models import ServiceRequest

def manage_requests(request):
    requests = ServiceRequest.objects.all()
    return render(request, 'support/manage_requests.html', {'requests': requests})