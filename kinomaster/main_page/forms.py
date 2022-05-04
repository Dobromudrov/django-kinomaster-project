from django import forms

# from movies.models import *

from movies.models import Reviews


class ReviewForm(forms.ModelForm):
    """Reviews form"""
    class Meta:
        model = Reviews
        fields = ("name", "text")

