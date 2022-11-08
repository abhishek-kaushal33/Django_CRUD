from cProfile import label
from django import forms
from django.core import validators
from . models import User

# def mail(value):
#     if "@" not in value:
#         raise forms.ValidationError("Please enter valid email address") 

# Normal Form

# class UserForm(forms.Form):
#     Username=forms.CharField(error_messages={"required":"Please enter username"})
#     Email=forms.EmailField(error_messages={"required":"Please enter e-mail address"})
#     Password=forms.CharField(widget=forms.PasswordInput,error_messages={"required":"Please enter password"})
#     Rpassword=forms.CharField(widget=forms.PasswordInput,label="Re-enter Password",error_messages={"required":"Please enter correct password"})


# ModelForm
 
class UserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=["username","email","password","rpassword"]
        labels={"rpassword":"Re-enter Password"}
        widgets={
            "username":forms.TextInput,
            "email":forms.EmailInput,
            "password":forms.PasswordInput,
            "rpassword":forms.PasswordInput,
        }

    def clean(self):
        cleaned_data=super().clean()
        valpass = self.cleaned_data["password"]
        Rpass = self.cleaned_data["rpassword"]
        if valpass != Rpass:
            raise forms.ValidationError("Please enter correct Password")
