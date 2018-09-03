from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<slug:sort>/card_list/', views.CardList, name='card_list'),
    path('<int:card_id>/items/', views.CardItems, name='card_items'),
]