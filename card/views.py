from django.shortcuts import render_to_response, render
from django.http import HttpResponse
from django.utils import timezone
from .models import Card

def index(request):
    return render(request, 'card/index.html', {})

def card_list(request):
    cards = Card.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    return render(request, 'card/card_list.html', {'cards': cards})
