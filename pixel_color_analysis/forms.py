from django import forms
from .models import *


class ImgForm(forms.ModelForm):
    class Meta:
        model = Images
        fields = ['img', 'hex_code']


class AnalysisForm(forms.ModelForm):
    class Meta:
        model = Analysis
        fields = ['comparison', 'num_pixels_hex']