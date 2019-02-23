from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import CreateView

from meals.forms import AddMealForm


class MealCreateView(LoginRequiredMixin, CreateView):
    template_name = 'meals/add.html'
    form_class = AddMealForm
    login_url = '/accounts/login/'

    def get(self, request, *args, **kwargs):
        return super(MealCreateView, self).get(request, *args, **kwargs)

    def form_valid(self, form):
        meal = form.save(commit=False)
        meal.user_id = self.request.user.pk
        meal.save()
        messages.success(self.request, 'success')
        return HttpResponseRedirect(reverse('meal-add'))
