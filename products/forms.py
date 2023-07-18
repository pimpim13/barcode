from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'country_id', 'manufacturer_id', 'number_id']
        labels = {'name': 'Produit',
                  'country_id': 'Code Pays (1)',
                  'manufacturer_id': 'Code Fournisseur (6)',
                  'number_id': 'Code Produit (5)'
                  }



