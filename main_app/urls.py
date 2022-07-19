from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('finches/', views.finch_index, name='index'),
    path('finches/<int:finch_id>/', views.finch_detail, name='detail'),
    path('finches/create/', views.FinchCreate.as_view(), name='finches_create'),
    path('finches/<int:pk>/update/', views.FinchUpdate.as_view(), name='finches_update'),
    path('finches/<int:pk>/delete/', views.FinchDelete.as_view(), name='finches_delete'),
    path('finches/<int:finch_id>/add_sighting/', views.add_sighting, name='add_sighting'),
    path('finches/<int:finch_id>/add_photo/', views.add_photo, name='add_photo'),
    path('finches/<int:finch_id>/assoc_region/<int:region_id>/', views.assoc_region, name='assoc_region'),
    path('finches/<int:finch_id>/delete_region/<int:region_id>/', views.delete_region, name='delete_region'),
    path('regions/', views.RegionList.as_view(), name='region_index'),
    path('regions/<int:pk>/', views.RegionCreate.as_view(), name='region_detail'),
    path('regions/create/', views.RegionCreate.as_view(), name='region_create'),
    path('regions/<int:pk>/update/', views.RegionUpdate.as_view(), name='region_update'),
    path('regions/<int:pk>/delete/', views.RegionDelete.as_view(), name='region_delete'),
    path('accounts/signup/', views.signup, name='signup'),
]