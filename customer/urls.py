from django.urls import path,include
from customer import views

urlpatterns = [
path('', views.welcome_home, name='welcome_home'),
path('contact_us', views.contactView, name='contactView'),
path('about', views.aboutView, name='aboutView'),
path('download', views.downloadView, name='downloadView'),
path('how_does_it_works', views.how_does_it_worksView, name='how_does_it_worksView'),
path('privacy_terms', views.privacy_termsView, name='privacy_termsView'),

]
