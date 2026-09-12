from django import forms

from .models import (
    Artisan,
    Craft,
)


class ArtisanForm(forms.ModelForm):
    class Meta:
        model = Artisan

        fields = [
            "name",
            "location",
            "region",
            "story",
            "profile_image",
            "practices",
        ]

        widgets = {
            "story": forms.Textarea(
                attrs={
                    "rows": 6,
                    "placeholder": (
                        "Tell us about yourself, "
                        "your craft and what you "
                        "would like people to know."
                    ),
                }
            ),
            "practices": forms.CheckboxSelectMultiple(),
        }


class CraftForm(forms.ModelForm):
    class Meta:
        model = Craft

        fields = [
            "name",
            "category",
            "description",
            "image",
            "process_video",
            "making_video",
            "price",
            "selling_method",
            "practices",
        ]

        widgets = {
            "description": forms.Textarea(
                attrs={
                    "rows": 6,
                    "placeholder": (
                        "Describe what you made, "
                        "how it is made, and what "
                        "makes it special."
                    ),
                }
            ),
            "practices": forms.CheckboxSelectMultiple(),
        }