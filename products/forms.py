from django.shortcuts import get_object_or_404
from django import forms
from .models import Product, Category, Image_upload, UserProfile


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]
        
        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'

        self.fields['discount_price'].widget.attrs['required'] = False

class Image_uploadForm(forms.ModelForm):
    """Form for the image model"""
    class Meta:
        model = Image_upload
        fields = ('title', 'image')

