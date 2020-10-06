from django import forms
from .models import blog


class blog(forms.ModelForm):

    class Meta:
        model = blog
        fields = ('title', 'description', 'image')
