from django import forms
from .models import *

class AddTenant(forms.ModelForm):

  class Meta:
    model = tenant
    fields = "__all__"

class UpdateTenant(forms.ModelForm):

  class Meta:
    model = tenant
    fields = ['apartment']

class AddRequest(forms.ModelForm):
  class Meta:
    model = requests
    fields = "__all__"
    exclude = ('apartment','status',)
