import graphene
from graphene import relay, ObjectType
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from apps.shop.models import Product


class CategoryNode(DjangoObjectType):
    class Meta:
        model = Product
        filter_fields = ["title", "slug"]
        interfaces = (relay.Node,)


# ['title', 'slug', 'price', 'sale', 'author', 'image_preview', 'image_alt']
class ProductNode(DjangoObjectType):
    class Meta:
        model = Product
        # Allow for some more advanced filtering here
        filter_fields = {
            "code": ["exact"],
            "title": ["exact"],
            "slug": ["exact"],
            "sale": ["exact"],
            "price": ["exact", "icontains", "istartswith"],
            "notes": ["exact", "icontains"],
            "author": ["exact"],
            "image_preview": ["exact"],
            "category": ["exact"],
            "category__title": ["exact"],
        }
        interfaces = (relay.Node,)


# 'code',
# 'title',
# 'slug',
# 'description',
# 'price',
# 'sale',
# 'categories',
# 'author',
# 'count',
# 'type_product',
# 'material',
# 'included',
# 'height',
# 'weight',
# 'colors',
# # ImagesMixin
# 'image_preview',
# 'image_alt',
# # SeoMixin
# 'title_seo',
# 'meta_keywords',
# 'meta_description',
# 'created_at',
# 'update_at'
# )


class Query(graphene.ObjectType):
    category = relay.Node.Field(CategoryNode)
    all_categories = DjangoFilterConnectionField(CategoryNode)

    # ingredient = relay.Node.Field(IngredientNode)
    # all_ingredients = DjangoFilterConnectionField(IngredientNode)
