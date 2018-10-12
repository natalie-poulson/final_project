from django.urls import path
from .  import views

app_name = "final_app"

urlpatterns = [
    path('', views.landing, name='landing'),

    path('profile/create', views.profile_create, name='profile_create'),
    path('profile/edit', views.profile_edit, name='profile_edit'),
    path('profile', views.profile_view, name="profile"),

    path('trips/<int:pk>', views.trip_detail, name="trip_detail"),
    path('trip/create', views.trip_create, name="trip_create"),

    path('posts/<int:pk>', views.post_detail, name="post_detail"),
    path('post/create', views.post_create, name="post_create"),

]
