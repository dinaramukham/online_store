from django import forms

from .models import Product, Version
from fuzzywuzzy import process
from .bad_words import bad_words


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ('photo',)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class']='form-control'
    def clean_name(self):
        cleaned_data = self.cleaned_data['name']
        result_comparison = process.extract(cleaned_data, bad_words)
        for result in result_comparison:
            if result[1] >= 50:
                raise forms.ValidationError('В названии товара замечены проблемные слова')
        return cleaned_data
    def clean_message(self):
        cleaned_data = self.cleaned_data['message']
        result_comparison = process.extract(cleaned_data, bad_words)
        for result in result_comparison:
            if result[1] >= 70:
                raise forms.ValidationError('Замечены проблемные слова')
        return cleaned_data
class VersionForm(forms.ModelForm  ):
    def __init__(self, *args, **kwargs ):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
    class Meta:
        model=Version
        fields='__all__'

