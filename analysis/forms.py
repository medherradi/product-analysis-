from django import forms
from .models import Purchase, Product 

class PurchaseForm(forms.ModelForm):
      product = forms.ModelChoiceField(queryset=Product.objects.all(),
                                      widget=forms.Select(attrs={'class':'input'})
                                      )
      class Meta:
            model = Purchase
            fields = ['product', 'price', 'quantity']
            widgets = {
                  'price': forms.NumberInput(attrs={'class':'input'}),
                  'quantity': forms.NumberInput(attrs={'class':'input'}),
            }
            
