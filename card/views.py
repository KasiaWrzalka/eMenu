from django.shortcuts import render_to_response, render
from django.http import HttpResponse
from django.utils import timezone
from .models import Card

def index(request):
    return render(request, 'card/index.html', {})

def CardList(request, sort):
    cards = Card.objects.filter(created_date__lte=timezone.now()).order_by('id')
    print(sort)
    if sort == 'name':
        cards = Card.objects.filter(created_date__lte=timezone.now()).order_by('name')
    elif sort == 'countR':
        cards = sorted(Card.objects.filter(created_date__lte=timezone.now()),
                       key=lambda i: i.carditem_set.all().count())
    elif sort == 'countM':
        cards = sorted(Card.objects.filter(created_date__lte=timezone.now()),
                       key=lambda i: i.carditem_set.all().count())[::-1]
    else:
        cards = Card.objects.filter(created_date__lte=timezone.now()).order_by('id')
    return render(request, 'card/card_list.html', {'cards': cards})

def CardItems(request, card_id):
    items = Card.objects.get(id=card_id).carditem_set.all()
    return render(request, 'card/card_items.html', {'items': items})
