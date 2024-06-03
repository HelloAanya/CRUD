# home/urls.py
# home/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.Add, name='add'),
    path('edit/', views.Edit, name='edit'),
    path('update/<str:id>/', views.Update, name='update'),
    path('delete/<str:id>/', views.Delete, name='delete')

]
