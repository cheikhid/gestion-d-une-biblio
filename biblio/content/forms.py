from django import forms
from .models import Book, Category


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = [
            'name'
        ]
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'})
        }

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = [
            'title',
            'image_book',
            'author',
            'image_author',
            'page',
            'price',
            'rental_price_day',
            'rental_period',
            'rental_total',
            'status',
            'category',
            
        ]
        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'image_book':forms.FileInput(attrs={'class':'form-control'}),
            'author':forms.TextInput(attrs={'class':'form-control'}),
            'image_author':forms.FileInput(attrs={'class':'form-control'}),
            'page':forms.NumberInput(attrs={'class':'form-control'}),

            'price':forms.NumberInput(attrs={'class':'form-control'}),
            'rental_price_day':forms.NumberInput(attrs={'class':'form-control','id':'rentalprice'}),
            'rental_period':forms.NumberInput(attrs={'class':'form-control','id':'rentalday'}),
            'rental_total':forms.NumberInput(attrs={'class':'form-control','id':'rentaltotal'}),
            'status':forms.Select(attrs={'class':'form-control'}),
            'category':forms.Select(attrs={'class':'form-control'}),
        }