from django.shortcuts import (
    get_object_or_404,
    redirect,
    render,
)

from .forms import ArtisanForm, CraftForm
from .models import (
    Artisan,
    Craft,
    Practice,
)


def marketplace(request):
    """
    KARIGAR homepage.
    """

    featured = (
        Craft.objects
        .filter(
            published=True,
            featured=True,
        )
        .select_related("artisan")
        .prefetch_related("practices")
        .first()
    )

    crafts = (
        Craft.objects
        .filter(published=True)
        .select_related("artisan")
        .prefetch_related("practices")
        .order_by("-created_at")
    )

    practices = Practice.objects.all()[:6]

    artisans = (
        Artisan.objects
        .prefetch_related("practices")
        .order_by("-created_at")[:6]
    )

    return render(
        request,
        "marketplace/marketplace.html",
        {
            "featured": featured,
            "crafts": crafts,
            "practices": practices,
            "artisans": artisans,
        },
    )


def discover(request):
    """
    Full craft discovery page.
    """

    crafts = (
        Craft.objects
        .filter(published=True)
        .select_related("artisan")
        .prefetch_related("practices")
        .order_by("-created_at")
    )

    return render(
        request,
        "marketplace/discover.html",
        {
            "crafts": crafts,
        },
    )


def craft_detail(request, slug):
    """
    Public craft page.
    """

    craft = get_object_or_404(
        Craft.objects
        .select_related("artisan")
        .prefetch_related("practices"),
        slug=slug,
        published=True,
    )

    return render(
        request,
        "marketplace/craft_detail.html",
        {
            "craft": craft,
        },
    )


def artisans(request):
    """
    Artisan directory.
    """

    artisans_list = (
        Artisan.objects
        .prefetch_related("practices")
        .order_by("name")
    )

    return render(
        request,
        "marketplace/artisans.html",
        {
            "artisans": artisans_list,
        },
    )


def artisan_detail(request, slug):
    """
    Public KARIGAR ID / artisan profile.
    """

    artisan = get_object_or_404(
        Artisan.objects.prefetch_related(
            "practices",
            "crafts",
        ),
        slug=slug,
    )

    crafts = (
        artisan.crafts
        .filter(published=True)
        .prefetch_related("practices")
        .order_by("-created_at")
    )

    return render(
        request,
        "marketplace/artisan_detail.html",
        {
            "artisan": artisan,
            "crafts": crafts,
        },
    )


def practices(request):
    """
    Practice directory.
    """

    practices_list = Practice.objects.all()

    return render(
        request,
        "marketplace/practices.html",
        {
            "practices": practices_list,
        },
    )


def practice_detail(request, slug):
    """
    Practice detail page.
    """

    practice = get_object_or_404(
        Practice.objects.prefetch_related(
            "artisans",
            "crafts",
        ),
        slug=slug,
    )

    artisans_list = practice.artisans.all()
    crafts = practice.crafts.filter(
        published=True
    )

    return render(
        request,
        "marketplace/practice_detail.html",
        {
            "practice": practice,
            "artisans": artisans_list,
            "crafts": crafts,
        },
    )


def atlas(request):
    """
    Initial Craft Atlas.
    """

    practices_list = (
        Practice.objects
        .all()
        .order_by("region", "name")
    )

    return render(
        request,
        "marketplace/atlas.html",
        {
            "practices": practices_list,
        },
    )


def stories(request):
    """
    Story discovery page.
    """

    artisans_list = (
        Artisan.objects
        .exclude(story="")
        .prefetch_related("practices")
        .order_by("-created_at")
    )

    return render(
        request,
        "marketplace/stories.html",
        {
            "artisans": artisans_list,
        },
    )


def add_craft(request):
    """
    Artisan onboarding / craft submission.
    """

    if request.method == "POST":
        artisan_form = ArtisanForm(
            request.POST,
            request.FILES,
        )

        craft_form = CraftForm(
            request.POST,
            request.FILES,
        )

        if (
            artisan_form.is_valid()
            and craft_form.is_valid()
        ):
            artisan = artisan_form.save()

            craft = craft_form.save(
                commit=False
            )

            craft.artisan = artisan
            craft.published = True
            craft.save()

            craft_form.save_m2m()

            return redirect(
                "craft_success"
            )

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