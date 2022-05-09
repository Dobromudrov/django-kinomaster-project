from django import forms

from movies.models import *

from movies.models import Reviews


class ReviewForm(forms.ModelForm):
    """Reviews form"""
    class Meta:
        model = Reviews
        fields = ("name", "text")


class RatingForm(forms.ModelForm):
    star = forms.ModelChoiceField(
        queryset=RatingStar.objects.all(), widget=forms.RadioSelect(), empty_label=None
    )

    class Meta:
        model = Rating
        fields = ("star",)