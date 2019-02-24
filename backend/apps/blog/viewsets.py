from rest_framework.viewsets import ModelViewSet
from .serializer import ArticleSerializer
from .models import Article


class ArticleList(ModelViewSet):
    """ Posts viewset
    ```
    Там есть типо json ниже, такой не подойдет?
    {
        "id": 3,
        "title": "str",
        "slug": "str",
        "content": "str",
        "is_active": true(boolen),
        "author": null,
        "tags": [
            {
                'id': 1,
                'title': 'srt',
                'slug': 'srt',
            }
        ],
        "image_preview": 'str:path',
        "image_alt": 'str',
        "title_seo": "str",
        "meta_keywords": "str",
        "meta_description": "str",
        "created_at": "2018-11-13T13:41:06.274000Z",
        "update_at": "2018-11-13T13:41:06.274000Z"
    }
    ```
    """
    queryset = Article.objects.prefetch_related('tags').all()
    serializer_class = ArticleSerializer
    http_method_names = ['get']
