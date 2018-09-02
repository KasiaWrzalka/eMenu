from django.shortcuts import render_to_response, render
from django.http import HttpResponse
from django.utils import timezone
from .models import Card

def index(request):
    return render(request, 'card/index.html', {})

def CardList(request):
    cards = Card.objects.filter(created_date__lte=timezone.now()).order_by('id')
    c2 = Card.objects.filter(id=3)
    for i in c2:
        print((i.carditem_set.all().count()))
    return render(request, 'card/card_list.html', {'cards': cards})

def CardItems(request, card_id):
    items = Card.objects.get(id=card_id).carditem_set.all()
    return render(request, 'card/card_items.html', {'items': items})
