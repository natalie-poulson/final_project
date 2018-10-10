from django.urls import path
from final_app import views

urlpatterns = [
    path('', views.index, name='index')
]
