from django import forms
from website import models

class IndividualForm(forms.ModelForm):
    class Meta:
        model = models.Individual
        fields = [ 'name', 'email', 'phone', 'occupation']