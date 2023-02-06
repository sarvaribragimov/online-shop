from django import forms

from ..models.review import Review

class ReviewForm(forms.Form):
    class Meta:
        model = Review
        fields = ["desc","rating"]
        widgets = {
            "desc":forms.Textarea(attrs={"class":"form-control"}),
            "rating":forms.NumberInput(attrs={"class":"form-control"}),
        }