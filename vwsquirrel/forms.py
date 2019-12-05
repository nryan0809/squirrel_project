from django.forms import ModelForm
from .models import sq_model
class SquForm(ModelForm):
    class Meta:
        model = sq_model
        fields = '__all__'
