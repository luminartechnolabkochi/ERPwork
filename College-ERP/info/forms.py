from django import forms
from django.forms  import ModelForm
from django.contrib.auth.models import User
from .models import Accountant,FeeManager,Payroll
from django.contrib.auth.forms import UserCreationForm

class UserRegistrationForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))

    class Meta:
        model=User
        fields=["username","email","password1","password2"]

        widgets={
            "username":forms.TextInput(attrs={"class":"form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),

        }


class AccountantForm(ModelForm):
    class Meta:
        model=Accountant
        fields=["name","sex","DOB","salary"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "sex": forms.TextInput(attrs={"class": "form-control"}),
            "salary": forms.NumberInput(attrs={"class": "form-control"}),
            "DOB":forms.DateInput(attrs={"class":"form-control"})

        }

class SalaryForm(ModelForm):
    class Meta:
        model=Payroll
        fields=["accountnumber",
                "pannum",
                "num_working_days",
                "num_leave",
                "salary"]
        widgets={
            "accountnumber":forms.TextInput(attrs={"class":"form-control"}),
            "pannum":forms.TextInput(attrs={"class":"form-control"}),
            "num_working_days": forms.TextInput(attrs={"class": "form-control"}),
            "num_leave": forms.TextInput(attrs={"class": "form-control"}),
            "salary":forms.NumberInput(attrs={"class":"form-control"}),


        }


class FeesPaymentForm(ModelForm):
    confirm_acno=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    class Meta:
        model=FeeManager
        fields=["to_acno","confirm_acno","amount"]
        widgets={
            "to_acno":forms.PasswordInput(attrs={"class":"form-control"}),
            "amount":forms.NumberInput(attrs={"class":"form-control"})
        }
    def clean(self):
        cleaned_data=super().clean()
        to_acno=cleaned_data.get("to_acno")
        confirm_acno=cleaned_data.get("confirm_acno")
        if to_acno !=confirm_acno:
            msg="account number mis match"
            self.add_error("to_acno",msg)