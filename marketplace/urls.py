from django.urls import path
from . import views

urlpatterns = [
    path("", views.marketplace, name="marketplace"),

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

    path(
        "craft/<int:craft_id>/",
        views.craft_detail,
        name="craft_detail",
    ),
]