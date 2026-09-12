from django.urls import path
from . import views


urlpatterns = [
    # Home
    path(
        "",
        views.marketplace,
        name="marketplace",
    ),

    # Discovery
    path(
        "discover/",
        views.discover,
        name="discover",
    ),

    # Crafts
    path(
        "craft/<slug:slug>/",
        views.craft_detail,
        name="craft_detail",
    ),

    # Artisans
    path(
        "artisans/",
        views.artisans,
        name="artisans",
    ),

    path(
        "artisan/<slug:slug>/",
        views.artisan_detail,
        name="artisan_detail",
    ),

    # Practices
    path(
        "practices/",
        views.practices,
        name="practices",
    ),

    path(
        "practice/<slug:slug>/",
        views.practice_detail,
        name="practice_detail",
    ),

    # Atlas
    path(
        "atlas/",
        views.atlas,
        name="atlas",
    ),

    # Stories
    path(
        "stories/",
        views.stories,
        name="stories",
    ),

    # Artisan creation
    path(
        "artisan/add/",
        views.add_craft,
        name="add_craft",
    ),

    path(
        "artisan/success/",
        views.craft_success,
        name="craft_success",
    ),
]