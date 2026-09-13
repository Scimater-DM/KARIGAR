from django.contrib import admin

from .models import Artisan, Practice, Craft, Auction


@admin.register(Artisan)
class ArtisanAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "location",
        "region",
        "created_at",
    )

    search_fields = (
        "name",
        "location",
        "region",
        "story",
    )

    prepopulated_fields = {
        "slug": ("name",),
    }


@admin.register(Practice)
class PracticeAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "region",
    )

    search_fields = (
        "name",
        "region",
        "description",
    )

    prepopulated_fields = {
        "slug": ("name",),
    }


@admin.register(Craft)
class CraftAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "artisan",
        "category",
        "selling_method",
        "price",
        "minimum_price",
        "created_at",
    )

    search_fields = (
        "name",
        "category",
        "description",
        "artisan__name",
    )

    list_filter = (
        "category",
        "selling_method",
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
        "current_price",
        "ends_at",
        "is_active",
    )

    search_fields = (
        "craft__name",
    )

    list_filter = (
        "is_active",
    )