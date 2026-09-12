from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Practice(models.Model):
    name = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(
        max_length=170,
        unique=True,
        blank=True,
    )
    short_description = models.CharField(
        max_length=300,
        blank=True,
    )
    cultural_context = models.TextField(blank=True)
    region = models.CharField(
        max_length=150,
        blank=True,
    )
    image = models.ImageField(
        upload_to="practices/",
        blank=True,
        null=True,
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse(
            "practice_detail",
            kwargs={"slug": self.slug},
        )


class Artisan(models.Model):
    name = models.CharField(max_length=100)

    slug = models.SlugField(
        max_length=170,
        unique=True,
        blank=True,
    )

    location = models.CharField(
        max_length=150,
    )

    region = models.CharField(
        max_length=100,
        blank=True,
    )

    story = models.TextField(blank=True)

    profile_image = models.ImageField(
        upload_to="artisans/",
        blank=True,
        null=True,
    )

    verified = models.BooleanField(
        default=False,
    )

    practices = models.ManyToManyField(
        Practice,
        blank=True,
        related_name="artisans",
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse(
            "artisan_detail",
            kwargs={"slug": self.slug},
        )


class Craft(models.Model):
    SELLING_METHODS = [
        ("fixed", "Fixed Price"),
        ("offer", "Accept Offers"),
        ("auction", "Auction"),
    ]

    artisan = models.ForeignKey(
        Artisan,
        on_delete=models.CASCADE,
        related_name="crafts",
    )

    name = models.CharField(
        max_length=200,
    )

    slug = models.SlugField(
        max_length=170,
        unique=True,
        blank=True,
    )

    category = models.CharField(
        max_length=100,
    )

    description = models.TextField(
        blank=True,
    )

    image = models.ImageField(
        upload_to="crafts/",
        blank=True,
        null=True,
    )

    process_video = models.URLField(
        blank=True,
    )

    making_video = models.URLField(
        blank=True,
        null=True,
    )

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
    )

    selling_method = models.CharField(
        max_length=20,
        choices=SELLING_METHODS,
        default="fixed",
    )

    published = models.BooleanField(
        default=False,
    )

    featured = models.BooleanField(
        default=False,
    )

    practices = models.ManyToManyField(
        Practice,
        blank=True,
        related_name="crafts",
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)

        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse(
            "craft_detail",
            kwargs={"slug": self.slug},
        )


class Auction(models.Model):
    craft = models.OneToOneField(
        Craft,
        on_delete=models.CASCADE,
        related_name="auction",
    )

    starting_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
    )

    current_bid = models.DecimalField(
        max_digits=10,
        decimal_places=2,
    )

    end_time = models.DateTimeField()

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    def __str__(self):
        return f"Auction — {self.craft.name}"