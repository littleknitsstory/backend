import graphene
from graphene import relay
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from src.apps.shop.models import Product


class CategoryNode(DjangoObjectType):
    class Meta:
        model = Product
        filter_fields = ["title", "slug"]
        interfaces = (relay.Node,)


class ProductNode(DjangoObjectType):
    class Meta:
        model = Product
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


class Query(graphene.ObjectType):
    category = relay.Node.Field(CategoryNode)
    all_categories = DjangoFilterConnectionField(CategoryNode)
