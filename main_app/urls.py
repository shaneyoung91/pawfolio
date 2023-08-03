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
    path('dogs/<int:dog_id>/reportcard_detail/<int:reportcard_id>/', views.reportcard_detail, name='reportcard_detail'),
    path('dogs/<int:pk>/reportcard_update/<int:reportcard_id>/', views.ReportCardUpdate.as_view(), name='reportcard_update'),
    path('dogs/<int:pk>/reportcard_delete/', views.ReportCardDelete.as_view(), name='reportcard_delete'),
    path('accounts/signup/', views.signup, name='signup'),
    path('treats/', views.TreatList.as_view(), name='treats_index'),
    
    # CIRCLE BACK - ADDING DOG TREAT ON DOG INDEX PAGE
    path('treats/add_treat', views.add_treat, name='add_treat'),
    # -------------------------------
    
    path('dogs/<int:dog_id>/assoc_treat/<int:treat_id>/', views.assoc_treat, name='assoc_treat'),
    path('dogs/<int:dog_id>/unassoc_treat/<int:treat_id>/', views.unassoc_treat, name='unassoc_treat'),
    path('dogs/<int:dog_id>/add_photo/', views.add_photo, name='add_photo'),
]
