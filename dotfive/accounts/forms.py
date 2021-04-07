from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import Item

DATE_INPUT_FORMATS = ['%d-%m-%Y']

my_default_errors = {
    'required': '* Required',
    'invalid': 'Invalid',
    'unique': 'Is used'
}

# Categories by default for Items
CATEGORY_CHOICES = (
		('Category1', 'Category 1'),
		('Category2', 'Category 2'),
		('Category3', 'Category 3'),
	) 

class ItemForm(ModelForm):
	label = forms.CharField(required=True, max_length=150, label='label', error_messages=my_default_errors, help_text='100 characters max.', widget=forms.fields.TextInput(attrs={'placeholder': 'Label Item'}))
	category = forms.ChoiceField(choices = CATEGORY_CHOICES)
	
	class Meta:
		model = Item
		fields = [
			"label",
			"category"
		]

class CreateNewUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']