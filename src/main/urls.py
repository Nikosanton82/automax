from django.urls import path
from .views import main_view, tours_view, reservation, reservation_success

urlpatterns = [
    path('', main_view, name='main'),
    path('tours', tours_view, name='tours'),
    path('reservation_form/', reservation, name='reservation'),
    path('reservation_success/', reservation_success, name='reservation_success'),
]