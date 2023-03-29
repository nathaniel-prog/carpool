from django.db import models
from django.contrib.auth.models import User
from twilio.rest import Client

from twilio.twiml.messaging_response import  MessagingResponse
from .secret import key_auth_token , key_account_sid
from .direct import *
from twilio.twiml import (
    TwiML,
    format_language,
)

from phonenumber_field.modelfields import PhoneNumberField

# assuming obj is a model instance

from .insert_function import with_city
from django.contrib import admin
import requests
import datetime
import pytz
import urllib
import json
from django.contrib import messages

from django.urls import reverse
import phonenumbers
import phonenumber_field
from django.conf import settings
from django.core import validators
from phonenumbers.util import unicod

from django.utils import timezone

moi = User.objects.get(id=2)








now = timezone.now()

dt_mtn=datetime.datetime.now(tz=pytz.timezone('Asia/Jerusalem'))


res = requests.get('https://ipinfo.io/')
data= res.json()
place=(data['city'])
now = datetime.datetime.now()


class Offre(models.Model):
    ville=models.CharField(max_length=150 , default=place, null=True)
    depart = models.CharField(max_length=150, default=place, null=True, verbose_name='indiquez votre ville et adresse de depart ou un lieu')
    arrive = models.CharField(max_length=150, null=False, default='tel-aviv',verbose_name='indiquez votre destination final  ')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    passagers = models.PositiveIntegerField(null=False, verbose_name='indiquez le nombre de place disponible ')

    num_phone = PhoneNumberField(null=True, default='+972')
    date_depart = models.DateTimeField(auto_now_add=False, default=now , null= True)



    def __str__(self):
        return f" votre trajet from {self.depart} to {self.arrive} est prevu ce jour ci {self.date_depart.strftime('%d-%m-%Y')} "

    def get_absolute_url(self):
        return reverse('home')


    def save(self , *args , **kwargs):

        account_sid = key_account_sid
        auth_token = key_auth_token


        if self.author and self.num_phone:

            client = Client(account_sid, auth_token)

            message = client.messages.create(
                body=f' salut  {self.depart} {self.arrive}  {self.__str__()}',

                from_='+12543312099',
                to='+972505552709',

            )
        print(message.sid)

        return super().save(*args, **kwargs)







class Post(models.Model):
    ville=models.CharField(max_length=150,default=place, null=False)
    depart= models.CharField(max_length=150, default=place, null=True , verbose_name='indiquez votre adresse de depart')
    arrive= models.CharField(max_length=150, null=True ,default='', verbose_name='indiquez votre adresse d arrivé' )
    adresse=models.CharField(max_length=150, null=False )
    author= models.ForeignKey(User,on_delete=models.CASCADE )
    passagers= models.PositiveIntegerField(null=True , verbose_name='indiquez le nombre de personnes ')
    baggages = models.PositiveIntegerField(null=True, verbose_name=' bagagges etc ..')
    num_phone = PhoneNumberField(null=True, default='+972')
    date = models.DateTimeField(auto_now_add=False, default=now)
    exp_date=models.DateTimeField( auto_now_add=False , default=now)



    def __str__(self):
        return f" {self.author} are looking for a carpool from  {self.depart} to {self.arrive} "


    def get_absolute_url(self):
        return reverse('user_post')












    def timesup(self):
        now = datetime.datetime.now()
        get=Post.objects.filter(self.date<now)
        tdelta2 = datetime.timedelta(seconds=100)
        # print(tdelta2)
        sous = now - tdelta2

        if get < sous:
            get.delete()











class Chauffeur(models.Model):
    name= models.CharField(max_length=125 , null=False)
    car= models.CharField(max_length=255 ,default='Regular car', null=False)
    car_image = models.ImageField(default='hotelsample.jpg', upload_to='images/', null=True)
    num_phone = PhoneNumberField(unique=True, null=True, default='+972')
    client = models.ManyToManyField(User , related_name='user_client')
    passager= models.PositiveIntegerField(null=True)



    def __str__(self):
        return str(self.name)

    def place_dispo(self):
        nbr_passager= self.passager
        return "je dispose encore de {} place(s) disponible " .format(nbr_passager)



    def save(self , *args , **kwargs):

        account_sid = key_account_sid
        auth_token = key_auth_token


        if self.name and self.num_phone:

            client = Client(account_sid, auth_token)

            message = client.messages.create(
                body=f' salut  comment va tu ? привет как она идет? ',

                from_='+12543312099',
                to= f'{self.num_phone}',
            )
        print(message.sid)

        return super().save(*args, **kwargs)


    def sms_reply(self):
        resp=MessagingResponse()
        resp.message('shalom shalom shalom')
        return str(resp)

if __name__ == '__main__':
	print('yes')










