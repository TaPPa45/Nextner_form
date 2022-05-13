from .models import Products 
from django.forms import ModelForm

class ProductsForm(ModelForm):
    class Meta:
        model = Products
        fields = ['title', 'product_type', 'delivery_date', 'file_attachment', 'address']
        