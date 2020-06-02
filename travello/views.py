from django.shortcuts import render
from .models import Destination
# Create your views here.


def index(request):
    # dest1 = Destination()
    # dest1.name = 'Mumbai'
    # dest1.desc = 'The City Never sleep '
    # dest1.img = 'destination_1.jpg'
    # dest1.price = 700
    # dest1.offer = False
    #
    # dest2 = Destination()
    # dest2.name = 'Hyderabad'
    # dest2.desc = 'The City Nizam '
    # dest2.img = 'destination_2.jpg'
    # dest2.price = 500
    # dest2.offer = True
    #
    # dest3 = Destination()
    # dest3.name = 'Banglore'
    # dest3.desc = 'The City of Mysoor '
    # dest3.img = 'destination_3.jpg'
    # dest3.price = 800
    # dest3.offer = True

    dests = Destination.objects.all()

    return render(request, 'index.html', {'dests': dests})
