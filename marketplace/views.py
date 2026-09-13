from django.shortcuts import get_object_or_404, redirect, render

from .forms import ArtisanForm, CraftForm
from .models import Artisan, Craft, Practice


def marketplace(request):
    crafts = (
        Craft.objects
        .select_related("artisan")
        .prefetch_related("practices")
    )

    practices = Practice.objects.all()
    artisans_list = Artisan.objects.all()

    return render(
        request,
        "marketplace/marketplace.html",
        {
            "crafts": crafts,
            "practices": practices,
            "artisans": artisans_list,
        },
    )


def artisans(request):
    artisans_list = Artisan.objects.prefetch_related("crafts")

    return render(
        request,
        "marketplace/artisans.html",
        {
            "artisans": artisans_list,
        },
    )


def artisan_detail(request, slug):
    artisan = get_object_or_404(
        Artisan.objects.prefetch_related("crafts"),
        slug=slug,
    )

    return render(
        request,
        "marketplace/artisan_details.html",
        {
            "artisan": artisan,
        },
    )


def craft_detail(request, slug):
    craft = get_object_or_404(
        Craft.objects.select_related("artisan").prefetch_related("practices"),
        slug=slug,
    )

    return render(
        request,
        "marketplace/craft_detail.html",
        {
            "craft": craft,
        },
    )


def practices(request):
    practices_list = Practice.objects.all()

    return render(
        request,
        "marketplace/practices.html",
        {
            "practices": practices_list,
        },
    )


def practice_detail(request, slug):
    practice = get_object_or_404(
        Practice.objects.prefetch_related("crafts"),
        slug=slug,
    )

    return render(
        request,
        "marketplace/practice_detail.html",
        {
            "practice": practice,
        },
    )


def add_craft(request):
    if request.method == "POST":
        artisan_form = ArtisanForm(request.POST, request.FILES)
        craft_form = CraftForm(request.POST, request.FILES)

        if artisan_form.is_valid() and craft_form.is_valid():
            artisan = artisan_form.save()

            craft = craft_form.save(commit=False)
            craft.artisan = artisan
            craft.save()
            craft_form.save_m2m()

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
        "marketplace/craft_success.html",
    )

def artisan_home(request):
    return render(request, "marketplace/artisan_home.html")