import datetime

from django import forms

from meals.models import Meal

BREAKFAST_MEAL_COUNT = (
    (0, '0'),
    (0.5, '0.5'),
    (1, '1'),
    (1.5, '1.5'),
    (2, '2'),
    (2.5, '2.5'),
)

LUNCH_DINNER_MEAL_COUNT = (
    (0, '0'),
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, '4'),
    (5, '5'),
)


class AddMealForm(forms.ModelForm):
    meal_date = forms.DateField(
        label='Add meal for',
        widget=forms.TextInput(
            attrs={'class': 'form-control d-inline w-30 mr-2', 'id': 'mealDate'}),
        initial=datetime.datetime.now().date())
    breakfast = forms.ChoiceField(choices=BREAKFAST_MEAL_COUNT, widget=forms.Select(attrs={'class': 'form-control'}),
                                  initial=0.5)
    lunch = forms.ChoiceField(choices=LUNCH_DINNER_MEAL_COUNT, widget=forms.Select(attrs={'class': 'form-control'}),
                              initial=1)
    dinner = forms.ChoiceField(choices=LUNCH_DINNER_MEAL_COUNT, widget=forms.Select(attrs={'class': 'form-control'}),
                               initial=1)

    class Meta:
        model = Meal
        fields = ('meal_date', 'breakfast', 'lunch', 'dinner')
