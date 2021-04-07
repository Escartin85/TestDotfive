from django.test import TestCase

from .models import Item
# Create your tests here.

# Class for Test the Item Class
class ItemTest(TestCase):
    
    def setUp(self):
        self.item = Item()
        self.item.label = "Hello_Test"
        self.item.slug = "hello_test"
        self.item.category = "Category1"
        self.item.save()
        
        record = Item.items.get(slug="hello_test")
        self.assertEqual(record, self.item)
        
    def test_slug_on_save(self):
        self.item = Item()
        self.item.label = "Hello_Testing"
        self.item.category = "Category1"
        self.item.save()
        
        self.assertEqual(self.item.slug, "hello_testing")
        