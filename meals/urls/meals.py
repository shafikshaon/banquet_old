from django.urls import path

from meals.views import MealCreateView

urlpatterns = [
    path('add/', MealCreateView.as_view(), name='meal-add'),
]
