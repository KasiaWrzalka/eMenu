from django.shortcuts import render_to_response, render
from django.core.paginator import Paginator
from django.http import HttpResponse, JsonResponse
from django.utils import timezone
from .models import Card, CardSerializer

def index(request):
    return render(request, 'card/index.html', {})

def CardList(request):
    cards_list = [i for i in Card.objects.filter(created_date__lte=timezone.now()).order_by('id')
                  if i.carditem_set.all().count() > 0]

    paginator = Paginator(cards_list, 2)

    page = request.GET.get('page')
    cards = paginator.get_page(page)

    return render(request, 'card/card_list.html', {'cards': cards, 'pages': range(1, paginator.num_pages+1)})


def CardItems(request, card_id):
    card = Card.objects.get(id=card_id)
    items = card.carditem_set.all()
    return render(request, 'card/card_items.html', {'items': items, 'card': card})

def getCards(request):
    sort = request.GET.get('sort')
    page = request.GET.get('page')
    if sort == 'name':
        cards = Card.objects.all().order_by('name')
    elif sort == 'countR':
        cards = sorted(Card.objects.all(), key=lambda i: i.carditem_set.all().count())
    elif sort == 'countM':
        cards = sorted(Card.objects.all(), key=lambda i: i.carditem_set.all().count())[::-1]
    else:
        cards = Card.objects.all().order_by('id')

    cards = [i for i in cards if i.carditem_set.all().count() > 0]

    paginator = Paginator(cards, 2)

    cards = paginator.get_page(page)

    serializer = CardSerializer(cards, many=True)
    return JsonResponse(serializer.data, safe=False)
