from django.urls import path

from .import views
from django.contrib.auth.views import LoginView , LogoutView
from django.conf import settings
from django.conf.urls.static import static
from .views import DeletePostView, ChauffeurListView, \
    ChauffeurDetail, PostListView, DetailPostView, CreatePostView, CreateOfferView,\
    PostUpdateView, OfferListView ,UserDetail

urlpatterns = [


   path('', views.home , name='home'),
    path('logout', LogoutView.as_view(template_name= 'logout.html'),name='logout'),
    path('post<int:pk>delete', DeletePostView.as_view(), name='postdelete'),
    path('where', views.where , name='where'),
    path('users',PostListView.as_view(),name='post-list'),
    path('offres',OfferListView.as_view(),name='offre-list'),
    path('user/<str:username>',PostListView.as_view(),name='user_post'),
    path('post<int:pk>',DetailPostView.as_view(), name='postdetail'),
    path('post/<int:pk>/update',PostUpdateView.as_view(), name='post_update'),
    path('chauffeurs', ChauffeurListView.as_view(), name='chauffeurs_list'),
    path('chauffeur<int:pk>' , ChauffeurDetail.as_view(), name='chauffeur'),
    path('carinfo', views.infocar , name='infocar'),
    path('ask', views.ask_dest , name='ask'),
    path('info', views.infocovoiturage, name= 'infocovoiturage'),
    path('post/new', CreatePostView.as_view(), name='create'),
    path('offre/new', CreateOfferView.as_view() , name='create_offer'),
    path('sms', views.envoi_sms, name='sendsms'),
    path('voir', views.OffreCov, name='voir'),
    path('user_id/<int:pk> ',UserDetail.as_view(), name='user_id'),
    path('list/(?P<letter>[a-z])$',views.st_view(), name="lis_view")






]



if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)