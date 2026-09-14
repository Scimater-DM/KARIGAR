import json
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from .forms import ArtisanForm, CraftForm
from .models import Artisan, Craft, Practice
from .services.saathi_ai import ask_saathi_agent, catalog_craft_with_saathi


def marketplace(request):
    crafts = Craft.objects.select_related("artisan").prefetch_related("practices")
    practices_list = Practice.objects.all()
    artisans_list = Artisan.objects.prefetch_related("crafts")

    hero_craft = crafts.filter(
        image__isnull=False
    ).exclude(
        image=""
    ).first()

    featured_crafts = crafts.filter(
        image__isnull=False
    ).exclude(
        image=""
    )

    featured_artisans = artisans_list.filter(
        profile_image__isnull=False
    ).exclude(
        profile_image=""
    )

    return render(
        request,
        "marketplace/marketplace.html",
        {
            "crafts": crafts,
            "hero_craft": hero_craft,
            "featured_crafts": featured_crafts,
            "practices": practices_list,
            "artisans": artisans_list,
            "featured_artisans": featured_artisans,
        },
    )


def crafts(request):
    qs = Craft.objects.select_related("artisan").prefetch_related("practices")

    query = request.GET.get("q", "").strip()
    category = request.GET.get("category", "").strip()
    region = request.GET.get("region", "").strip()

    if query:
        from django.db.models import Q
        qs = qs.filter(
            Q(name__icontains=query)
            | Q(category__icontains=query)
            | Q(artisan__name__icontains=query)
            | Q(artisan__location__icontains=query)
        )

    if category:
        qs = qs.filter(category__iexact=category)

    if region:
        qs = qs.filter(artisan__region__iexact=region)

    categories = (
        Craft.objects
        .exclude(category="")
        .values_list("category", flat=True)
        .distinct()
        .order_by("category")
    )

    regions = (
    Artisan.objects
    .exclude(region="")
    .values_list("region", flat=True)
    .distinct()
    .order_by("region")
)

    return render(
        request,
        "marketplace/crafts.html",
        {
            "crafts": qs,
            "query": query,
            "category": category,
            "region": region,
            "categories": categories,
            "regions": regions,
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


def artisan_home(request):
    return render(
        request,
        "marketplace/artisan_home.html",
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
        Craft.objects
        .select_related("artisan")
        .prefetch_related("practices"),
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
        artisan_form = ArtisanForm(
            request.POST,
            request.FILES,
        )

        craft_form = CraftForm(
            request.POST,
            request.FILES,
        )

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


@csrf_exempt
@require_http_methods(["POST"])
def saathi_chat_api(request):
    try:
        data = json.loads(request.body.decode("utf-8")) if request.body else {}
    except Exception:
        data = request.POST.dict()

    query = data.get("query") or data.get("message") or ""
    action = data.get("action", "general")
    context = data.get("context", {})
    language = data.get("language", "auto")

    result = ask_saathi_agent(query=query, action=action, context=context, language=language)
    return JsonResponse(result)


@csrf_exempt
@require_http_methods(["POST"])
def saathi_catalog_api(request):
    try:
        data = json.loads(request.body.decode("utf-8")) if request.body else {}
    except Exception:
        data = request.POST.dict()

    transcript = data.get("transcript") or data.get("text") or ""
    result = catalog_craft_with_saathi(transcript=transcript)
    return JsonResponse(result)
