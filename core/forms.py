from django import forms

#Search form
class SearchForm(forms.Form):
    query = forms.CharField(label='Search', max_length=100)
