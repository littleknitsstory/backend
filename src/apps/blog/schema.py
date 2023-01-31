import graphene
from graphene import ObjectType
from graphene_django import DjangoObjectType

from src.apps.blog.models import Tag, Article


class TagsType(DjangoObjectType):
    class Meta:
        model = Tag


class ArticleType(DjangoObjectType):
    class Meta:
        model = Article


class Query(ObjectType):
    all_tags = graphene.List(TagsType)
    all_articles = graphene.List(ArticleType)

    def resolve_all_categories(self, info, **kwargs):

        return Tag.objects.all()

    def resolve_all_articles(self, info, **kwargs):
        return Article.objects.prefetch_related("tags").all()
