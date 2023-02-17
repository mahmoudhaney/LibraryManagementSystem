from django import forms
from .models import *

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = [
            'title',
            'author',
            'photo_book',
            'photo_author',
            'pages',
            'price',
            'retal_price_day',
            'retal_peroid',
            'total_retal',
            'status',
            'category_id',
        ]

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control'}),
            'photo_book': forms.FileInput(attrs={'class': 'form-control'}),
            'photo_author': forms.FileInput(attrs={'class': 'form-control'}),
            'pages': forms.NumberInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'retal_price_day': forms.NumberInput(attrs={'class': 'form-control', 'id':'rentalprice'}),
            'retal_peroid': forms.NumberInput(attrs={'class': 'form-control', 'id':'rentaldays'}),
            'total_retal': forms.NumberInput(attrs={'class': 'form-control', 'id':'totalrental'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'category_id': forms.Select(attrs={'class': 'form-control'}),
        }