from django.contrib.sitemaps import Sitemap

from src.apps.blog.models.models import Article
from src.apps.shop.models import Category
from src.apps.shop.models import Product


class I18nSitemap(Sitemap):
    protocol = "http"
    i18n = True

    def location(self, obj):
        return f"/{obj.slug}"


class ProductSitemap(I18nSitemap):
    def items(self):
        return Product.objects.only("id", "title").order_by("-id")

    def location(self, obj):
        return f"/products/{obj.slug}"


class CategorySitemap(I18nSitemap):
    def items(self):
        categories = Category.objects.all().order_by("id")
        return categories.only("id", "title", "slug")

    def location(self, obj):
        return f"/categories/{obj.slug}"


class ArticleSitemap(I18nSitemap):
    def items(self):
        posts = Article.objects.filter(is_active=True)
        return posts.only("id", "title", "slug")

    def location(self, obj):
        return f"/posts/{obj.slug}"


sitemaps = {
    "categories": CategorySitemap,
    "products": ProductSitemap,
    "pages": ArticleSitemap,
}
