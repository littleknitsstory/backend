from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import status
from django.template import Template, Context
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.viewsets import ViewSet

from src.apps.convert_pdf.serializers import DataSerializer


class ChatCompletionViewSet(ViewSet):
    serializer = DataSerializer
    renderer_classes = (TemplateHTMLRenderer,)

    def list(self, request):
        template_str = """<!DOCTYPE html>
        <html>
            <head>
                <style>
                    body {
                        font-family: DejaVu Sans, sans-serif;
                    }
                </style>
            </head>
            <body>
               <p>{{ content }}</p>
            </body>
        </html>"""
        template = Template(template_str)
        serializer = self.serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        content = data["choices"][0]["message"]["content"]
        context = Context({"content": content})
        rendered_template = template.render(context)
        return HttpResponse(
            rendered_template, content_type="text/html", status=status.HTTP_200_OK
        )
