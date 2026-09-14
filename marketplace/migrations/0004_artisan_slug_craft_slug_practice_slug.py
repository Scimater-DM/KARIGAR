from django.db import migrations, models
from django.utils.text import slugify


def populate_slugs(apps, schema_editor):
    Artisan = apps.get_model("marketplace", "Artisan")
    Craft = apps.get_model("marketplace", "Craft")
    Practice = apps.get_model("marketplace", "Practice")

    def make_unique_slug(value, used):
        base = slugify(value) or "item"
        slug = base
        number = 2

        while slug in used:
            slug = f"{base}-{number}"
            number += 1

        used.add(slug)
        return slug

    used = set()
    for artisan in Artisan.objects.all().order_by("id"):
        artisan.slug = make_unique_slug(artisan.name, used)
        artisan.save(update_fields=["slug"])

    used = set()
    for craft in Craft.objects.all().order_by("id"):
        craft.slug = make_unique_slug(craft.name, used)
        craft.save(update_fields=["slug"])

    used = set()
    for practice in Practice.objects.all().order_by("id"):
        practice.slug = make_unique_slug(practice.name, used)
        practice.save(update_fields=["slug"])


class Migration(migrations.Migration):

    dependencies = [
        ("marketplace", "0003_practice_artisan_practices_craft_practices"),
    ]

    operations = [
        migrations.AddField(
            model_name="artisan",
            name="slug",
            field=models.SlugField(
                blank=True,
                null=True,
                max_length=170,
                db_index=False,
            ),
        ),
        migrations.AddField(
            model_name="craft",
            name="slug",
            field=models.SlugField(
                blank=True,
                null=True,
                max_length=170,
                db_index=False,
            ),
        ),
        migrations.AddField(
            model_name="practice",
            name="slug",
            field=models.SlugField(
                blank=True,
                null=True,
                max_length=170,
                db_index=False,
            ),
        ),
        migrations.RunPython(
            populate_slugs,
            reverse_code=migrations.RunPython.noop,
        ),
        migrations.AlterField(
            model_name="artisan",
            name="slug",
            field=models.SlugField(
                blank=True,
                max_length=170,
                unique=True,
                db_index=False,
            ),
        ),
        migrations.AlterField(
            model_name="craft",
            name="slug",
            field=models.SlugField(
                blank=True,
                max_length=170,
                unique=True,
                db_index=False,
            ),
        ),
        migrations.AlterField(
            model_name="practice",
            name="slug",
            field=models.SlugField(
                blank=True,
                max_length=170,
                unique=True,
                db_index=False,
            ),
        ),
    ]