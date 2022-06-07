from django import forms

from app.models import book, LoginInfo_Table


class Book_Form(forms.ModelForm):
    class Meta:
        model = book
        fields = "__all__"


class Register_Form(forms.ModelForm):
    class Meta:
        model = LoginInfo_Table
        fields = "__all__"
