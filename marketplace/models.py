from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Artisan(models.Model):
    name = models.CharField(max_length=120)
    location = models.CharField(max_length=120)
    region = models.CharField(max_length=120, blank=True)
    story = models.TextField(blank=True)
    profile_image = models.ImageField(
        upload_to="artisans/",
        blank=True,
        null=True,
    )
    slug = models.SlugField(max_length=140, unique=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["name"]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("artisan_detail", kwargs={"slug": self.slug})

    def __str__(self):
        return self.name


class Practice(models.Model):
    name = models.CharField(max_length=120)
    region = models.CharField(max_length=120)
    description = models.TextField(blank=True)
    image = models.ImageField(
        upload_to="practices/",
        blank=True,
        null=True,
    )
    slug = models.SlugField(max_length=140, unique=True, blank=True)

    class Meta:
        ordering = ["name"]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("practice_detail", kwargs={"slug": self.slug})

    def __str__(self):
        return self.name


class Craft(models.Model):
    SELLING_FIXED = "fixed"
    SELLING_OFFERS = "offers"
    SELLING_AUCTION = "auction"

    SELLING_METHODS = [
        (SELLING_FIXED, "Fixed Price"),
        (SELLING_OFFERS, "Accept Offers"),
        (SELLING_AUCTION, "Auction"),
    ]

    artisan = models.ForeignKey(
        Artisan,
        on_delete=models.CASCADE,
        related_name="crafts",
    )

    name = models.CharField(max_length=160)
    category = models.CharField(max_length=120)
    description = models.TextField()

    image = models.ImageField(
        upload_to="crafts/",
        blank=True,
        null=True,
    )

    making_video = models.URLField(
        blank=True,
        null=True,
        help_text="YouTube or other process video link.",
    )

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True,
    )

    minimum_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True,
        help_text="The minimum price the artisan is willing to accept.",
    )

    selling_method = models.CharField(
        max_length=20,
        choices=SELLING_METHODS,
        default=SELLING_FIXED,
    )

    slug = models.SlugField(max_length=180, unique=True, blank=True)
    practices = models.ManyToManyField(
        Practice,
        blank=True,
        related_name="crafts",
    )

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("craft_detail", kwargs={"slug": self.slug})

    def __str__(self):
        return self.name


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

    current_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
    )

    ends_at = models.DateTimeField()

    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["ends_at"]

    def __str__(self):
        return f"Auction — {self.craft.name}"