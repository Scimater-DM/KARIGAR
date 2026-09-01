from django.db import models


class Artisan(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    story = models.TextField(blank=True)
    profile_image = models.ImageField(
        upload_to="artisans/",
        blank=True,
        null=True
    )
    verified = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Craft(models.Model):
    SELLING_METHODS = [
        ("fixed", "Fixed Price"),
        ("offer", "Accept Offers"),
        ("auction", "Auction"),
    ]

    artisan = models.ForeignKey(
        Artisan,
        on_delete=models.CASCADE,
        related_name="crafts"
    )

    name = models.CharField(max_length=200)
    category = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(
        upload_to="crafts/",
        blank=True,
        null=True
    )
    process_video = models.URLField(blank=True)
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )
    making_video = models.URLField(
        blank=True, 
        null=True)
    selling_method = models.CharField(
        max_length=20,
        choices=SELLING_METHODS,
        default="fixed"
    )
    published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Auction(models.Model):
    craft = models.OneToOneField(
        Craft,
        on_delete=models.CASCADE,
        related_name="auction"
    )

    starting_price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    current_bid = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    end_time = models.DateTimeField()

    def __str__(self):
        return f"Auction - {self.craft.name}"