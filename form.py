from django import forms

from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import  Chauffeur , Post, Offre
from django.apps import apps








class Info_Car(forms.Form):
    marque= forms.CharField()
    modele= forms.CharField()
    photo=forms.FileField()



class ChauffeurCov(forms.ModelForm):
    class Meta:
        model = Chauffeur
        fields=['name', 'num_phone']



class Ask_destination(forms.ModelForm):
    class Meta:
        model= Offre
        fields=['depart', 'arrive','author', 'num_phone', 'passagers' ]

        widgets = {
            'depart': forms.TextInput(attrs={ 'placeholder':' ex haifa'})}


class OffreCov(forms.ModelForm):
    class Meta:
        model= Offre
        fields=['depart', 'arrive', 'num_phone', 'passagers', 'ville' ]

        widgets = {
            'depart': forms.TextInput(attrs={ 'placeholder':' votre adresse ou renseigner un lieu precis'}),
        'arrive': forms.TextInput(attrs={'placeholder': 'une adresse ou renseignez un lieu precis'}),

        }



