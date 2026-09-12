from django.contrib import admin

from .models import (
    Artisan,
    Auction,
    Craft,
    Practice,
)


@admin.register(Practice)
class PracticeAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "region",
        "created_at",
    )

    search_fields = (
        "name",
        "region",
    )

    prepopulated_fields = {
        "slug": ("name",),
    }


@admin.register(Artisan)
class ArtisanAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "location",
        "region",
        "verified",
        "created_at",
    )

    list_filter = (
        "verified",
        "region",
    )

    search_fields = (
        "name",
        "location",
        "region",
    )

    prepopulated_fields = {
        "slug": ("name",),
    }

    filter_horizontal = (
        "practices",
    )


@admin.register(Craft)
class CraftAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "artisan",
        "category",
        "price",
        "selling_method",
        "published",
        "featured",
        "created_at",
    )

    list_filter = (
        "published",
        "featured",
        "selling_method",
        "category",
    )

    search_fields = (
        "name",
        "category",
        "artisan__name",
    )

    prepopulated_fields = {
        "slug": ("name",),
    }

    filter_horizontal = (
        "practices",
    )


@admin.register(Auction)
class AuctionAdmin(admin.ModelAdmin):
    list_display = (
        "craft",
        "starting_price",
        "current_bid",
        "end_time",
    )

    search_fields = (
        "craft__name",
    )