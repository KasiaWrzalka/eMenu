from django.test import TestCase
from card.models import Card, CardItem
from django.utils import timezone

class CardTest(TestCase):

    def create_card(self, name="only a test", description="yes, this is only a test"):
        return Card.objects.create(name=name, description=description, created_date=timezone.now(), )

    def test_card_creation(self):
        w = self.create_card()
        self.assertTrue(isinstance(w, Card))
        self.assertEqual(w.__unicode__(), w.name)


class CardItemTest(TestCase):

    def create_card_item(self, name="only a test", description="yes, this is only a test"):
        return CardItem.objects.create(name=name, description=description, created_date=timezone.now(), )

    def test_card_item_creation(self):
        w = self.create_card()
        self.assertTrue(isinstance(w, CardItem))
        self.assertEqual(w.__unicode__(), w.name)
