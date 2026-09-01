from django import forms
from .models import Artisan, Craft


class ArtisanForm(forms.ModelForm):
    class Meta:
        model = Artisan
        fields = ["name", "location", "story", "profile_image"]


class CraftForm(forms.ModelForm):
    class Meta:
        model = Craft
        fields = [
            "name",
            "category",
            "description",
            "image",
            "process_video",
            "price",
            "selling_method",
        ]