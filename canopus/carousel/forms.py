from django import forms

class ImageForm(forms.Form):
    name = forms.CharField(max_length=50, required=True)
    description = forms.CharField(max_length=200, required=False)
    image = forms.ImageField()