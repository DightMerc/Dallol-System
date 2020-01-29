from django import forms

from .models import OnlineRieltor, CommonRieltorUser, Order

class PostForm(forms.ModelForm):

    class Meta:
        model = OnlineRieltor
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'photo': forms.FileInput(),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'description_UZ': forms.Textarea(attrs={'class': 'form-control'}),

            
        }
        fields = ('name', 'photo','description','description_UZ')


class PostForm2(forms.ModelForm):

    class Meta:
        model = Order
        
        fields = ('property','title', 'region', 'reference', 'room_count', 'square', 'area', 'main_floor', 'floor', 'state', 'ammount', 'add_info', 'contact', 'photo')