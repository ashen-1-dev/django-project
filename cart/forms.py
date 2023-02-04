from django import forms

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 11)]  # диапазон добавляемого количества товара


class CartAddProductForm(forms.Form):
  quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int, label='Количество товара')
  override = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)

