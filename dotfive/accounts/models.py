from django.db import models

# Create your models here.
# Class Model of Item
class Item(models.Model):
	CATEGORY = (
			('Category1', 'Category 1'),
			('Category2', 'Category 2'),
            ('Category3', 'Category 3'),
			) 

	label = models.CharField(max_length=200, null=True)
	category = models.CharField(max_length=200, null=True, choices=CATEGORY)
	date_created = models.DateTimeField(auto_now_add=True, null=True)

	def __str__(self):
		return self.label