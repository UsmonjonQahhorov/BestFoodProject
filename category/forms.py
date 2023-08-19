from django import forms

from category.models import Category


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__"
        widget = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "created_at": forms.DateInput(attrs={"class": "form-control"}),
            "updated_at": forms.DateInput(attrs={"class": "form-control"}),
        }