from django import forms

from .models import OnlineRieltor, CommonRieltorUser

class PostForm(forms.ModelForm):

    class Meta:
        model = OnlineRieltor
        fields = ('name', 'photo','description','description_UZ')


class PostForm2(forms.ModelForm):

    class Meta:
        model = CommonRieltorUser
        fields = ('name', 'user','rieltor')