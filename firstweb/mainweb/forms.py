from django import forms
from django.core.exceptions import ValidationError


class SearchForm(forms.Form):
    product_name = forms.CharField(max_length=200)
    price_min = forms.IntegerField()
    price_max = forms.IntegerField()

    def clean(self):
        cleaned_data = super().clean()
        price_min = cleaned_data.get('price_min')

        price_max = cleaned_data.get('price_max')
        print(price_min, "max", price_max)

        if(int(price_min) > int(price_max)):
            print("ini jalan")
            raise ValidationError(
                "Tidak boleh price minimum diatas price maksimum")

        return self.cleaned_data
