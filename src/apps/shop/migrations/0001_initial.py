# Generated by Django 4.1.2 on 2023-04-04 07:37

import colorful.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields
import optimized_image.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=120, verbose_name="Title")),
                (
                    "title_ru",
                    models.CharField(max_length=120, null=True, verbose_name="Title"),
                ),
                (
                    "title_en",
                    models.CharField(max_length=120, null=True, verbose_name="Title"),
                ),
                (
                    "slug",
                    django_extensions.db.fields.AutoSlugField(
                        blank=True,
                        editable=False,
                        populate_from="title",
                        verbose_name="slug",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Created at"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="Updated at"),
                ),
            ],
            options={
                "verbose_name": "Category",
                "verbose_name_plural": "Categories",
            },
        ),
        migrations.CreateModel(
            name="OrderCart",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "order_number",
                    django_extensions.db.fields.ShortUUIDField(
                        blank=True, editable=False, verbose_name="Number order"
                    ),
                ),
                (
                    "address",
                    models.CharField(
                        blank=True, max_length=256, null=True, verbose_name="Address"
                    ),
                ),
                (
                    "phone",
                    models.CharField(
                        blank=True, max_length=13, null=True, verbose_name="Phone"
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        blank=True, max_length=254, null=True, verbose_name="Email"
                    ),
                ),
                (
                    "comments",
                    models.CharField(
                        blank=True, max_length=512, null=True, verbose_name="Comments"
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Created"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="Updated at"),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("NEW", "New"),
                            ("AWAITING", "Awaiting pay"),
                            ("CREATING", "Creating"),
                            ("SHIPPING", "Shipping"),
                            ("COMPLETED", "Completed"),
                            ("CANCELED", "Canceled"),
                        ],
                        default="NEW",
                        max_length=14,
                        verbose_name="Status",
                    ),
                ),
                (
                    "order_total_cost",
                    models.DecimalField(
                        blank=True,
                        decimal_places=2,
                        default=0,
                        max_digits=14,
                        verbose_name="Total cost order",
                    ),
                ),
                (
                    "currency",
                    models.CharField(
                        default="EUR", max_length=3, verbose_name="Currency"
                    ),
                ),
            ],
            options={
                "verbose_name": "Order",
                "verbose_name_plural": "Orders",
                "ordering": ("-created_at",),
            },
        ),
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "image_preview",
                    optimized_image.fields.OptimizedImageField(
                        blank=True, upload_to="", verbose_name="Images"
                    ),
                ),
                (
                    "image_alt",
                    models.CharField(
                        blank=True, max_length=255, verbose_name="Images Alt"
                    ),
                ),
                ("title", models.CharField(max_length=120, verbose_name="Title")),
                (
                    "title_ru",
                    models.CharField(max_length=120, null=True, verbose_name="Title"),
                ),
                (
                    "title_en",
                    models.CharField(max_length=120, null=True, verbose_name="Title"),
                ),
                (
                    "code",
                    models.IntegerField(db_index=True, verbose_name="Code product"),
                ),
                (
                    "slug",
                    django_extensions.db.fields.AutoSlugField(
                        blank=True,
                        editable=False,
                        populate_from="title",
                        verbose_name="slug",
                    ),
                ),
                ("is_active", models.BooleanField(default=True, verbose_name="Active")),
                (
                    "description",
                    models.TextField(blank=True, null=True, verbose_name="Description"),
                ),
                (
                    "description_ru",
                    models.TextField(blank=True, null=True, verbose_name="Description"),
                ),
                (
                    "description_en",
                    models.TextField(blank=True, null=True, verbose_name="Description"),
                ),
                (
                    "price",
                    models.DecimalField(
                        blank=True,
                        decimal_places=2,
                        default=0,
                        max_digits=14,
                        verbose_name="Price",
                    ),
                ),
                (
                    "sale",
                    models.DecimalField(
                        blank=True,
                        decimal_places=2,
                        default=0,
                        max_digits=14,
                        verbose_name="Sale",
                    ),
                ),
                (
                    "currency",
                    models.CharField(
                        default="EUR", max_length=3, verbose_name="Currency"
                    ),
                ),
                (
                    "count",
                    models.IntegerField(blank=True, default=1, verbose_name="Count"),
                ),
                (
                    "type_product",
                    models.CharField(
                        blank=True,
                        max_length=120,
                        null=True,
                        verbose_name="Type Product",
                    ),
                ),
                (
                    "type_product_ru",
                    models.CharField(
                        blank=True,
                        max_length=120,
                        null=True,
                        verbose_name="Type Product",
                    ),
                ),
                (
                    "type_product_en",
                    models.CharField(
                        blank=True,
                        max_length=120,
                        null=True,
                        verbose_name="Type Product",
                    ),
                ),
                (
                    "material",
                    models.CharField(
                        blank=True, max_length=120, null=True, verbose_name="Material"
                    ),
                ),
                (
                    "material_ru",
                    models.CharField(
                        blank=True, max_length=120, null=True, verbose_name="Material"
                    ),
                ),
                (
                    "material_en",
                    models.CharField(
                        blank=True, max_length=120, null=True, verbose_name="Material"
                    ),
                ),
                (
                    "included",
                    models.CharField(
                        blank=True, max_length=120, null=True, verbose_name="Included"
                    ),
                ),
                (
                    "included_ru",
                    models.CharField(
                        blank=True, max_length=120, null=True, verbose_name="Included"
                    ),
                ),
                (
                    "included_en",
                    models.CharField(
                        blank=True, max_length=120, null=True, verbose_name="Included"
                    ),
                ),
                (
                    "height",
                    models.IntegerField(blank=True, null=True, verbose_name="Height"),
                ),
                (
                    "weight",
                    models.IntegerField(blank=True, null=True, verbose_name="Weight"),
                ),
                ("is_shipping_required", models.BooleanField(default=True)),
                ("is_digital", models.BooleanField(default=False)),
                (
                    "meta_title",
                    models.CharField(
                        blank=True, max_length=500, null=True, verbose_name="Title Seo"
                    ),
                ),
                (
                    "meta_title_ru",
                    models.CharField(
                        blank=True, max_length=500, null=True, verbose_name="Title Seo"
                    ),
                ),
                (
                    "meta_title_en",
                    models.CharField(
                        blank=True, max_length=500, null=True, verbose_name="Title Seo"
                    ),
                ),
                (
                    "meta_keywords",
                    models.TextField(blank=True, null=True, verbose_name="Keywords"),
                ),
                (
                    "meta_keywords_ru",
                    models.TextField(blank=True, null=True, verbose_name="Keywords"),
                ),
                (
                    "meta_keywords_en",
                    models.TextField(blank=True, null=True, verbose_name="Keywords"),
                ),
                (
                    "meta_description",
                    models.TextField(blank=True, null=True, verbose_name="Description"),
                ),
                (
                    "meta_description_ru",
                    models.TextField(blank=True, null=True, verbose_name="Description"),
                ),
                (
                    "meta_description_en",
                    models.TextField(blank=True, null=True, verbose_name="Description"),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Created at"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="Updated at"),
                ),
                (
                    "author",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="product_author",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "categories",
                    models.ManyToManyField(
                        blank=True,
                        related_name="product_categories",
                        to="shop.category",
                        verbose_name="Category",
                    ),
                ),
            ],
            options={
                "verbose_name": "Product",
                "verbose_name_plural": "Products",
                "ordering": ("-created_at",),
            },
        ),
        migrations.CreateModel(
            name="ProductColor",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("color", colorful.fields.RGBColorField(verbose_name="Color")),
            ],
            options={
                "verbose_name": "Product color",
                "verbose_name_plural": "Product colors",
            },
        ),
        migrations.CreateModel(
            name="ProductSimilar",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="similar_product",
                        to="shop.product",
                        verbose_name="Product",
                    ),
                ),
                (
                    "products",
                    models.ManyToManyField(
                        related_name="similar_products",
                        to="shop.product",
                        verbose_name="Products",
                    ),
                ),
            ],
            options={
                "verbose_name": ("Product Similar",),
                "verbose_name_plural": "Products Similar",
            },
        ),
        migrations.CreateModel(
            name="ProductPhoto",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "image_preview",
                    optimized_image.fields.OptimizedImageField(
                        blank=True, upload_to="", verbose_name="Images"
                    ),
                ),
                (
                    "image_alt",
                    models.CharField(
                        blank=True, max_length=255, verbose_name="Images Alt"
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="photo_product",
                        to="shop.product",
                        verbose_name="Product",
                    ),
                ),
            ],
            options={
                "verbose_name": "Product photo",
                "verbose_name_plural": "Product photos",
            },
        ),
        migrations.AddField(
            model_name="product",
            name="colors",
            field=models.ManyToManyField(
                blank=True,
                related_name="product_colors",
                to="shop.productcolor",
                verbose_name="Colors",
            ),
        ),
        migrations.CreateModel(
            name="OrderCartItem",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "amount",
                    models.PositiveSmallIntegerField(default=0, verbose_name="Amount"),
                ),
                (
                    "item_total_cost",
                    models.DecimalField(
                        blank=True,
                        decimal_places=2,
                        default=0,
                        max_digits=14,
                        verbose_name="Total cost item order",
                    ),
                ),
                (
                    "currency",
                    models.CharField(
                        default="EUR", max_length=3, verbose_name="Currency"
                    ),
                ),
                (
                    "order_cart",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="ordercartitem_ordercart",
                        to="shop.ordercart",
                        verbose_name="Order Cart",
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="ordercartitem_product",
                        to="shop.product",
                        verbose_name="Product",
                    ),
                ),
            ],
            options={
                "verbose_name": "Order Item",
                "verbose_name_plural": "Order Items",
            },
        ),
    ]
