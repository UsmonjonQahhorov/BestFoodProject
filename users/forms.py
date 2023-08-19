from django import forms

from users.models import User, TgUser


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = "__all__"
        widgets = {
            "firstname" : forms.TextInput(attrs={"class":"form-control"}),
            "lastname" : forms.TextInput(attrs={"class":"form-control"}),
            "role" : forms.Select(attrs={"class":"form-control"}),
            "created_at" : forms.DateInput(attrs={"class":"form-control"}),
            "updated_at" : forms.DateInput(attrs={"class":"form-control"}),
        }

class TgUserForm(forms.ModelForm):
    model = TgUser
    fields = "__all__"
    widgets = {
        "phone_number" : forms.TextInput(attrs={"class":"form"}),
        "fullname" : forms.TextInput(attrs={"class":"form-control"}),
        "is_blocked" : forms.TextInput(attrs={"class":"form-control"}),
        "created_at" : forms.DateInput(attrs={"class":"form-control"}),
        "updated_at" : forms.DateInput(attrs={"class":"form-control"}),
    }