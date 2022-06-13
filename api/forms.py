from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms  import UserCreationForm
from .models import Review,RATE_CHOICES


class regUserForm(UserCreationForm):
    username=forms.CharField(
        widget=forms.TextInput(attrs={'placeholder':'username', 'class':'form-field'}) )

    password1=forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder':'Password', 'class':'form-field'})
    )
    email=forms.CharField(
        widget=forms.EmailInput(attrs={'placeholder':'Email', 'class':'form-field'})
    )
    password2=forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder':' Confirm Password', 'class':'form-field'})
    )
    check_1=forms.BooleanField()
    check_2=forms.BooleanField()
    class Meta:
        model=User
        fields=['username', 'email' , 'password1', 'password2', 'check_1',  'check_2']


class ReviewForm(forms.ModelForm):
    review = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}),required=True)
    design = forms.ChoiceField(choices=RATE_CHOICES, widget= forms.Select(),required=True)
    usability = forms.ChoiceField(choices=RATE_CHOICES, widget= forms.Select(),required=True)
    content = forms.ChoiceField(choices=RATE_CHOICES, widget= forms.Select(),required=True)
    class Meta:
        model = Review
        fields = ['review', 'design','usability','content']