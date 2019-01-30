from django.forms import ModelForm
from .models import Candidate,Position

class PostForm(ModelForm):
    class Meta:
        model = Candidate
        exclude = ['id']
        exclude = ['position']
class PositionForm(ModelForm):
    class Meta:
        model = Position
        exclude = ['id']
