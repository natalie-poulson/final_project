from django.urls import path
from .  import views

app_name = "final_app"

urlpatterns = [
    path('', views.landing, name='landing'),

    path('profile/create', views.profile_create, name='profile_create'),
    path('profile/edit', views.profile_edit, name='profile_edit'),
    path('profile', views.profile_view, name="profile"),

    path('trips/<int:pk>', views.trip_detail, name="trip_detail"),
    path('trips/<int:pk>/edit', views.trip_edit, name="trip_edit"),
    path('trip/create', views.trip_create, name="trip_create"),
    path('trip/delete', views.trip_delete, name="trip_delete"),
    path('trips/completed', views.trips_completed, name="trips_completed"),
    path('trips/future', views.trips_future, name="trips_future"),

    path('posts/<int:pk>', views.post_detail, name="post_detail"),
    path('posts/<int:pk>/edit', views.post_edit, name="post_edit"),
    path('post/create', views.post_create, name="post_create"),
    path('post/delete', views.post_delete, name="post_delete"),

    path('gear/create', views.gear_create, name="gear_create"),
    path('gear/<int:pk>/edit', views.gear_edit, name="gear_edit"),
    path('gear/<int:pk>/delete', views.gear_delete, name="gear_delete"),
]
