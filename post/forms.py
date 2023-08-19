from django import forms

from post.models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = "__all__"
        widgets = {
            "title" : forms.TextInput(attrs={"class":"form-control"}),
            "content" : forms.TextInput(attrs={"class":"form-control"}),
            "image" : forms.ImageField(attrs={"class":"form-control"}),
            "status" : forms.Select(attrs={"class":"form-control"}),
            "created_at" : forms.DateInput(attrs={"class":"form-control"}),
            "updated_at" : forms.DateInput(attrs={"class":"form-control"})

        }