from django.urls import path

from . import views


urlpatterns = [
    path("", views.marketplace, name="marketplace"),
    path("artisans/", views.artisans, name="artisans"),
    path("artisan/add/", views.add_craft, name="add_craft"),
    path("artisan/success/", views.craft_success, name="craft_success"),
    path(
        "artisan/<slug:slug>/",
        views.artisan_detail,
        name="artisan_detail",
    ),
    path(
        "craft/<slug:slug>/",
        views.craft_detail,
        name="craft_detail",
    ),
    path("practices/", views.practices, name="practices"),
    path(
        "practice/<slug:slug>/",
        views.practice_detail,
        name="practice_detail",
    ),
]