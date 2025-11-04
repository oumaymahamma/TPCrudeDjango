from django.urls import path
from . import views

urlpatterns = [
    # exemple de route simple (page vide pour le moment)
    path('', views.BlogView.as_view(), name='blog_list'),
    path('create/', views.BlogCreateWithFields.as_view(), name='blog_create'),
    path('update/<int:pk>/', views.BlogUpdateView.as_view(), name='blog_update'),
    path('delete/<int:pk>/', views.BlogDeleteView.as_view(), name='blog_delete'),]