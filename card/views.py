from django.shortcuts import render_to_response, render
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.utils import timezone
from .models import Card

def index(request):
    return render(request, 'card/index.html', {})

def CardList(request, sort):
    if sort == 'name':
        cards_list = Card.objects.filter(created_date__lte=timezone.now()).order_by('name')
    elif sort == 'countR':
        cards_list = sorted(Card.objects.filter(created_date__lte=timezone.now()),
                       key=lambda i: i.carditem_set.all().count())
    elif sort == 'countM':
        cards_list = sorted(Card.objects.filter(created_date__lte=timezone.now()),
                       key=lambda i: i.carditem_set.all().count())[::-1]
    else:
        cards_list = Card.objects.filter(created_date__lte=timezone.now()).order_by('id')

    cards_list = [i for i in cards_list if i.carditem_set.all().count() > 0]

    paginator = Paginator(cards_list, 2)

    page = request.GET.get('page')
    cards = paginator.get_page(page)

    return render(request, 'card/card_list.html', {'cards': cards})

def CardItems(request, card_id):
    items = Card.objects.get(id=card_id).carditem_set.all()
    return render(request, 'card/card_items.html', {'items': items})
