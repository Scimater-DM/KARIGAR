from django import forms

from .models import Artisan, Craft


class ArtisanForm(forms.ModelForm):
    class Meta:
        model = Artisan
        fields = [
            "name",
            "location",
            "region",
            "story",
            "profile_image",
        ]

        widgets = {
            "name": forms.TextInput(
                attrs={
                    "placeholder": "Your name",
                }
            ),
            "location": forms.TextInput(
                attrs={
                    "placeholder": "Village, town or city",
                }
            ),
            "region": forms.TextInput(
                attrs={
                    "placeholder": "State or region",
                }
            ),
            "story": forms.Textarea(
                attrs={
                    "rows": 6,
                    "placeholder": (
                        "Tell us about yourself, "
                        "your craft and your journey."
                    ),
                }
            ),
        }


class CraftForm(forms.ModelForm):
    class Meta:
        model = Craft
        fields = [
            "name",
            "category",
            "description",
            "image",
            "making_video",
            "price",
            "minimum_price",
            "selling_method",
            "practices",
        ]

        widgets = {
            "name": forms.TextInput(
                attrs={
                    "placeholder": "What is your craft called?",
                }
            ),
            "category": forms.TextInput(
                attrs={
                    "placeholder": "e.g. Textiles, Pottery, Painting",
                }
            ),
            "description": forms.Textarea(
                attrs={
                    "rows": 6,
                    "placeholder": (
                        "Describe what you made, "
                        "how it is made, and what makes it special."
                    ),
                }
            ),
            "making_video": forms.URLInput(
                attrs={
                    "placeholder": "https://youtube.com/...",
                }
            ),
            "price": forms.NumberInput(
                attrs={
                    "step": "0.01",
                    "placeholder": "0.00",
                }
            ),
            "minimum_price": forms.NumberInput(
                attrs={
                    "step": "0.01",
                    "placeholder": "Minimum acceptable price",
                }
            ),
            "selling_method": forms.Select(),
            "practices": forms.CheckboxSelectMultiple(),
        }