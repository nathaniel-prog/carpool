from django.shortcuts import render , HttpResponse , redirect , get_object_or_404, reverse
from datetime import timedelta
from django.contrib.auth.decorators import login_required , permission_required
from django.db.models import Q
from .models import Post , User , Chauffeur , Offre
from .form import  Ask_destination , Info_Car , ChauffeurCov, OffreCov
from .insert_function import with_city
from django.http import HttpResponseRedirect
import time , timeit
from django.contrib.auth import login as auth_login
from django.contrib.auth import login as auth_login , authenticate
from django.contrib import messages
from michtamech.models import UserProfile
import calendar
from calendar import HTMLCalendar
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin ,UserPassesTestMixin
from django.views.generic import ListView, DetailView , CreateView,UpdateView , DeleteView
from django.contrib.auth import logout











def logout_view(request):
    logout(request)
    return redirect('home')





def home(request):
    post_= Post.objects.all()
    lastone = Offre.objects.last()




    profiles = UserProfile.objects.all()

    findlocal=with_city()


    if request.user.is_anonymous== True:
        return render(request,'home_for_annonimous.html', {'posts': post_ , 'profiles': profiles , 'lastone':lastone , findlocal:'findlocal' })
    else:
        return render(request, 'home.html', { 'findlocal':findlocal,'posts': post_ , 'profiles': profiles, 'lastone':lastone })





class PostListView(LoginRequiredMixin, ListView):
    model=Post
    fields = ['depart', 'arrivé', 'author']
    template_name = 'post_list.html'
    ordering = ['-id' ]
    paginate_by = 3



class  DetailPostView(LoginRequiredMixin, DetailView):
    model=Post
    template_name = 'post-detail.html'








class DeletePostView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Post
    template_name = 'post_confirm_delete.html'
    success_url = '/'

    def test_func(self):
        post= self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Post

    fields = ['depart', 'arrive',  'passagers']




    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post=self.get_object()
        if self.request.user==post.author:
            return True
        return False





def whereis(request):
    results= Post.object.filter(arrive='bengourion')
    return render(request, 'ousa.html', {'results':results})










class ChauffeurListView(ListView):
    model = Chauffeur
    template_name = 'chauffeur_list.html'




class ChauffeurDetail(DetailView):
    model= Chauffeur
    template_name = 'chauffeur.html'

    def get_context_data(self, *args,**kwargs):
        context=super(ChauffeurDetail, self).get_context_data()
        stuff = get_object_or_404(Chauffeur, id=self.kwargs['pk'])
        choosen = stuff.place_dispo()
        context['choosen']= choosen


        return context





class OfferListView(LoginRequiredMixin, ListView):
    model=Offre
    fields = ['depart', 'arrive', 'author']
    template_name = 'offer_list.html'
    ordering = ['-id' ]
    paginate_by = 3



class OffreDetail(DetailView):
    model= Offre
    template_name = 'user_info.html'

    def get_context_data(self, *args,**kwargs):
        context=super(OffreDetail, self).get_context_data()
        stuff = get_object_or_404(Offre, id=self.kwargs['pk'])
        choosen = stuff.save()
        context['choosen']= choosen


        return context

    def test_func(self):
        post=self.get_object()
        if self.request.user==post.author:
            return True
        return False




def infocar(request):
    return render(request,'car_covoiturage.html')


def ask_dest( request):

    if request.method == 'POST':
        form = Ask_destination(request.POST )
        titres= Offre.objects.all().filter(arrive=str(form.fields)).count()>2


        if form.is_valid():
            sform=form.save()

            return render(request ,'ask_desti.html',{'form':form , 'titres':titres , 'sform':sform} )

    else:
        form = Ask_destination()
        return render(request, 'ask_desti.html', {'form': form})



def offrecov( request):

    if request.method == 'POST':
        form =OffreCov(request.POST )
        titres= Offre.objects.filter(depart=str(form.fields))


        if form.is_valid():
            user=form.save()

            return render(request ,'offrecovo.html',{'form':form , 'titres':titres} )

    else:
        form = OffreCov()
        return render(request, 'offrecovo.html', {'form': form})


def infocovoiturage(request):
    if request.method == 'POST':
        new_form = ChauffeurCov(request.POST)
        if new_form.is_valid():
            user = new_form.save()
            return redirect( 'create_offer')

    else:
        new_form = ChauffeurCov()

    return render(request , 'covoit.html', {"form":new_form })





class CreateOfferView(LoginRequiredMixin,CreateView):
    model= Offre
    fields= ['depart', 'arrive','date_depart', 'passagers']

    template_name = 'offrecov.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)






class CreatePostView(LoginRequiredMixin,CreateView):
    model = Post
    fields=['depart','arrive', 'passagers']

    template_name = 'post_create.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)







def envoi_sms(request):
    if request.method == 'POST':
        form = OffreCov(request.POST)
        if form.is_valid():
            return render(request, 'sms.html', {'form': form})
    else:
        form= OffreCov()

        return render(request ,'sms.html',{'form':form} )


def where(request):
    if request.method == 'POST':
        query = request.POST["q1"]
        query2 = request.POST.get("q2")
        archives = Post.objects.filter(date=query2 ,arrive=query).count()>0
        archive = Post.objects.filter(arrive=query)
        offres=Offre.objects.filter(date=query2 ,arrive=query).count()>0
        if archives or offres:
            archive,offres
        else:
            messages.error(request, 'no one go there today')
        return render(request,'where.html', {'archive': archive ,  'archives':archives ,'offres':offres })




    else :
        if request.method== 'GET':
            return render(request,'where.html', )








