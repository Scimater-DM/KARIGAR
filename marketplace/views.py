from django.shortcuts import render, redirect
from .forms import ArtisanForm, CraftForm
from .models import Craft


def add_craft(request):
    if request.method == "POST":
        artisan_form = ArtisanForm(request.POST, request.FILES)
        craft_form = CraftForm(request.POST, request.FILES)

        if artisan_form.is_valid() and craft_form.is_valid():
            artisan = artisan_form.save()

            craft = craft_form.save(commit=False)
            craft.artisan = artisan
            craft.published = True
            craft.save()

            return redirect("craft_success")

    else:
        artisan_form = ArtisanForm()
        craft_form = CraftForm()

    return render(
        request,
        "marketplace/add_craft.html",
        {
            "artisan_form": artisan_form,
            "craft_form": craft_form,
        },
    )


def craft_success(request):
    return render(
        request,
        "marketplace/craft_success.html"
    )


def marketplace(request):
    crafts = Craft.objects.filter(
        published=True
    ).order_by("-created_at")

    return render(
        request,
        "marketplace/marketplace.html",
        {"crafts": crafts},
    )


def craft_detail(request, craft_id):
    craft = Craft.objects.get(id=craft_id)

    return render(
        request,
        "marketplace/craft_detail.html",
        {"craft": craft},
    )