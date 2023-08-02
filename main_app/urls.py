from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('dogs/', views.dogs_index, name='index'),
    path('dogs/<int:dog_id>/', views.dogs_detail, name='detail'),
    path('dogs/create/', views.DogCreate.as_view(), name='dogs_create'),
    path('dogs/<int:pk>/update/', views.DogUpdate.as_view(), name='dogs_update'),
    path('dogs/<int:pk>/delete/', views.DogDelete.as_view(), name='dogs_delete'),
    path('dogs/<int:dog_id>/add_reportcard/', views.add_reportcard, name='add_reportcard'),
    path('dogs/<int:dog_id>/reportcard_details/<int:reportcard_id>/', views.reportcard_details, name='reportcard_details'),
    path('accounts/signup/', views.signup, name='signup'),
    path('treats/', views.TreatList.as_view(), name='treats_index'),
    path('treats/create/', views.TreatCreate.as_view(), name='treats_create'),
    path('dogs/<int:dog_id>/assoc_treat/<int:treat_id>/', views.assoc_treat, name='assoc_treat'),
    path('dogs/<int:dog_id>/unassoc_treat/<int:treat_id>/', views.unassoc_treat, name='unassoc_treat'),
    path('dogs/<int:dog_id>/add_photo/', views.add_photo, name='add_photo'),
]
