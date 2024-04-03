from django.shortcuts import render
from .models import Car, Customer
# Create your views here.

# car list
def index(request):
    car = Car.objects.all()
    context = {
        "cars" : car
    }
    return render(request, template_name='business/index.html', context=context)

def customer_detail(request, customer_id):
    c = Customer.objects.get(id=customer_id)
    context = {
        "customer" : c
    }
    # 샘 알트먼 정보를 뽑아야 한다.
    pass
    # 뽑은 정보를 context에 담기 -> template로 보낸다.
    return render(request, template_name='business/customer_detail.html', context=context)