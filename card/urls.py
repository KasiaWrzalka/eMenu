from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('get_cards/', views.getCards, name='get_cards'),
    path('card_list/', views.CardList, name='card_list'),
    path('items/<int:card_id>', views.CardItems, name='card_items'),
]