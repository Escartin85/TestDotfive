from django.db import models
from django.urls import reverse
from django.db.models.signals import pre_save
from django.utils.text import slugify

# Create your models here.
# Class Worker Manager
class ItemManager(models.Manager):
	def active(self, *args, **kwargs):
		return super(ItemManager, self).all()

# Class Model of Item
class Item(models.Model):
    # Categories by default for Items
	CATEGORY = (
			('Category1', 'Category 1'),
			('Category2', 'Category 2'),
            ('Category3', 'Category 3'),
			) 

	label = models.CharField(max_length=200, blank=False, null=True)
	slug = models.SlugField(unique=True)
	category = models.CharField(max_length=200, null=True, choices=CATEGORY)
	date_created = models.DateTimeField(auto_now_add=True, null=True)

	# load all items in a list
	items = ItemManager()
 
	def __str__(self):
		return self.label

	# get absolute url resolved reversing by the slug for Item Detail
	def get_absolute_url(self):
		return reverse("itemDetail", kwargs={"slug":self.slug})

	# get absolute url resolved reversing by the slug for Item Update
	def get_url_edit(self):
		return reverse("itemUpdate", kwargs={"slug":self.slug})

	# get absolute url resolved reversing by the slug for Item Delete
	def get_url_delete(self):
		return reverse("itemDelete", kwargs={"slug":self.slug})

	class Meta:
		ordering = ["-label", "-date_created"]

# create a unique Slug and detect if an input Slug is repeat or unique
def create_slug(instance, new_slug=None):
	# Converting title in slug -> "Title article new 1" ==> "title-article-new-1"
	slug = slugify(instance.label + "_" + instance.category)
	
	if new_slug is not None:
		slug = new_slug
	qs = Item.items.filter(slug=slug).order_by("-id")
	exists = qs.exists()
	if exists:
		new_slug = "%s-%s" %(slug, qs.first().id)
		return create_slug(instance, new_slug=new_slug)
	return slug

# function load before save the Slug
def pre_save_item_reciver(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = create_slug(instance)



pre_save.connect(pre_save_item_reciver, sender=Item)