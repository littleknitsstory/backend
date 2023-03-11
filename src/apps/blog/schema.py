import graphene
from django.shortcuts import get_object_or_404
from graphene import ObjectType
from graphene_django import DjangoObjectType

from src.apps.account.models import User
from src.apps.blog.models import Tag, Article


class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = ("id", "username")


class TagsType(DjangoObjectType):
    class Meta:
        model = Tag
        fields = ("id", "title", "slug")


class ArticleType(DjangoObjectType):
    author = graphene.Field(UserType)

    class Meta:
        model = Article


class CreatePostInput(graphene.InputObjectType):
    title = graphene.String(required=True)
    content = graphene.String()
    author_id = graphene.ID(required=True)
    image_preview = graphene.String(required=True)


class UpdatePostInput(graphene.InputObjectType):
    title = graphene.String()
    slug = graphene.String()
    content = graphene.String()
    author_id = graphene.ID()
    image_preview = graphene.String()


class CreateArticleMutation(graphene.Mutation):
    class Arguments:
        input_data = CreatePostInput(required=True)
        tag_ids = graphene.List(graphene.ID)

    article = graphene.Field(ArticleType)

    def mutate(self, info, input_data, tag_ids):
        article = Article.objects.create(**input_data)

        if tag_ids:
            tags = Tag.objects.filter(id__in=tag_ids)
            article.tags.set(tags)

        return CreateArticleMutation(article=article)


class UpdateArticleMutation(graphene.Mutation):
    class Arguments:
        input_data = UpdatePostInput(required=True)
        id = graphene.ID(required=True)
        tag_ids = graphene.List(graphene.ID)

    article = graphene.Field(ArticleType)

    def mutate(self, info, input_data, id, tag_ids):
        article = get_object_or_404(Article, id=id)

        for key, value in input_data.items():
            setattr(article, key, value)

        article.save()

        if tag_ids:
            tags = Tag.objects.filter(id__in=tag_ids)
            article.tags.set(tags)

        return UpdateArticleMutation(article=article)


class DeleteArticleMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    ok = graphene.Boolean()

    def mutate(self, info, id):
        article = get_object_or_404(Article, id=id)

        article.delete()

        return DeleteArticleMutation(ok=True)


class Query(ObjectType):
    all_tags = graphene.List(TagsType)
    all_articles = graphene.List(ArticleType)
    article = graphene.Field(ArticleType, id=graphene.Int(required=True))

    def resolve_all_categories(self, info, **kwargs):
        return Tag.objects.all()

    def resolve_all_articles(self, info, **kwargs):
        return Article.objects.prefetch_related("tags", "author").all()

    def resolve_article(self, info, id):
        try:
            return Article.objects.prefetch_related("tags", "author").get(id=id)
        except Article.DoesNotExist:
            return None


class Mutation(graphene.ObjectType):
    create_article = CreateArticleMutation.Field()
    update_article = UpdateArticleMutation.Field()
    delete_article = DeleteArticleMutation.Field()
