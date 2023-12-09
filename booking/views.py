from django.shortcuts import render
from booking.models import Cardetail,Maketrip



def carview(request):
    c = Cardetail.objects.all()
    return render(request,'car.html',{'cars':c})


def car_details(request,p):
    d = Cardetail.objects.get(id=p) 
    return render(request,'car-single.html',{'detail':d})

def home(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def service(request):
    return render(request,'services.html')

def pricing(request):
    return render(request,'pricing.html')

def blog(request):
    return render(request,'blog.html')

def contact(request):
    return render(request,'contact.html')


def booking(request,p):
    if request.method == 'POST':
        pickup_loc = request.POST['pickup_l']
        dropoff_location = request.POST['dropoff_l']
        pickup_date = request.POST['pickup_d']
        dropoff_date = request.POST['dropoff_d']
        pickup_time = request.POST['pickup_t']
        d = Maketrip.objects.create(pickup = pickup_loc, dropoff = dropoff_location,pick_date = pickup_date,drop_date = dropoff_date,time = pickup_time)
        d.save()
    return render(request,'booking.html' ,{"id_car":p})


def booking_detail(request,b):
    # print("\n\n",b,"\n\n")
    booking = Maketrip.objects.get(id=b)
    detail = Cardetail.objects.get(id=b)
    return render(request,'booking_detail.html',{"booking_details":booking,"car_details": detail})
        
       
            
            
        