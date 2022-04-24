from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.MainView, name='home'),
    path('profile', views.profile, name='profile'),
    path('signup', views.register, name='registration'),
    path('add-achieve', views.add_achieve, name='achieve'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]