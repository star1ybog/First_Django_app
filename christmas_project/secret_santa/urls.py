from django.urls import path
from . import views

urlpatterns = [
    path('', views.is_it_christmas, name='home'),
    path('secret_santa/', views.secret_santa, name='secret_santa'),
    path('secret_santa/add/', views.add_participant, name='add_participant'),
    path('secret_santa/randomize/', views.randomize_pairs, name='randomize_pairs'),
    path('secret_santa/delete/<int:participant_id>/', views.delete_participant, name='delete_participant'),
]
