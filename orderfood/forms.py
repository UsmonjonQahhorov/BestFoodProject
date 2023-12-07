from django import forms

from orderfood.models import Order, Food, OrderFood


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = "__all__"
        widgets = {
            "total_price": forms.NumberInput(attrs={'class': 'form-control'}),
            "lat": forms.TextInput(attrs={'class': 'form-control'}),
            "lon": forms.TextInput(attrs={'class': 'form-control'}),
            "description": forms.TextInput(attrs={'class': 'form-control'}),
            "telegram_user": forms.Select(attrs={'class': 'form-control'}),
            "delivered_by": forms.Select(attrs={'class': 'form-control'}),
            "status": forms.Select(attrs={'class': 'form-control'}),
            "delivered_at": forms.DateInput(attrs={"class": "form-control"}),
            "created_at": forms.DateInput(attrs={"class": "form-control"}),
            "updated_at": forms.DateInput(attrs={"class": "form-control"})
        }


class FoodForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = "__all__"
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "description": forms.TextInput(attrs={"class": "form-control"}),
            "price": forms.NumberInput(attrs={"class": "form-control"}),
            "image": forms.URLInput(attrs={"class": "form-control"}),
            "category": forms.Select(attrs={"class": "form-control"}),
            "is_active": forms.TextInput(attrs={"class": "form-control"}),
            "created_at": forms.DateInput(attrs={"class": "form-control"}),
            "updated_at": forms.DateInput(attrs={"class": "form-control"}),
        }


class OrderFoodForm(forms.ModelForm):
    class Meta:
        model = OrderFood
        fields = "__all__"
        widgets = {
            "order": forms.Select(attrs={"class": "form-control"}),
            "food": forms.Select(attrs={"class": "form-control"}),
            "amount": forms.NumberInput(attrs={"class": "form-control"}),
            "price": forms.NumberInput(attrs={"class": "form-control"}),
            "created_at": forms.DateInput(attrs={"class": "form-control"}),
            "updated_at": forms.DateInput(attrs={"class": "form-control"}),
        }
