from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_credential/',views.add_credential),
    path('delete_credential/<int:credential_id>/', views.delete_credential)
]