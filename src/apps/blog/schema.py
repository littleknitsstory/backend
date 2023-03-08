import graphene
from graphene import ObjectType
from graphene_django import DjangoObjectType

from src.apps.account.models import User
from src.apps.blog.models import Tag, Article


class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = ('id', 'username')


class TagsType(DjangoObjectType):
    class Meta:
        model = Tag
        fields = ('id', 'title', 'slug')


class ArticleType(DjangoObjectType):
    author = graphene.Field(UserType)

    class Meta:
        model = Article
        fields = ('id', 'title', 'slug', 'content', 'is_active', 'author', 'tags')


class CreateArticleMutation(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)
        content = graphene.String(required=True)
        # author = graphene.ID(required=True)
        tags = graphene.List(graphene.Int)

    article = graphene.Field(ArticleType)

    def mutate(self, info,  title, content, tags):
        # author = User.objects.get(pk=author_id)
        article = Article(title=title, content=content)
        if tags:
            article.tags.set(tags)
        article.save()
        return CreateArticleMutation(article=article)


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
    article_mutation = CreateArticleMutation.Field()

