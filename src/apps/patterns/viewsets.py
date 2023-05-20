from io import BytesIO

from django.http import HttpResponse
from jinja2 import Template
from django.template import Context, Template
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.viewsets import ViewSet
from xhtml2pdf import pisa

from src.apps.patterns.models import Pattern
from src.apps.patterns.serializers import DataSerializer, PatternSerializer
from src.apps.patterns.services import fetch_data_from_api


class PatternViewset(ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Pattern.objects.all()
    http_method_names = ["post", "get"]
    lookup_field = "uuid"
    serializer_classes = {
        "create": PatternSerializer,
    }

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, PatternSerializer)

    def create(self, request, *args, **kwargs):
        serializer = PatternSerializer(data=request.data)
        if serializer.is_valid():
            prompt = serializer.validated_data["prompt"]
            completion = fetch_data_from_api(prompt)
            pattern = serializer.save(response=completion)
            return Response(
                {
                    "uuid": pattern.uuid,
                    "author": request.user.username,
                    "prompt": pattern.prompt,
                    "response": pattern.response,
                },
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ChatCompletionViewSet(ViewSet):
    serializer = DataSerializer
    renderer_classes = (TemplateHTMLRenderer,)

    def list(self, request, uuid=None):
        pattern = Pattern.objects.get(uuid=uuid)
        template_str = """<!DOCTYPE html>
                <html>
                    <head>
                        <style>
                            body {
                                font-family: DejaVu Sans, sans-serif;
                            }
                            p {
                                font-family: 'Times New Roman', Times, serif;
                            }
                        </style>
                    </head>
                    <body>
                       <p>{{ content }}</p>
                    </body>
                </html>"""
        template = Template(template_str)
        serializer = self.serializer(data=pattern.response)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        content = data["choices"][0]["message"]["content"]
        context = Context({"content": content})
        rendered_template = template.render(context)
        pdf_file = BytesIO()
        pisa.CreatePDF(
            BytesIO(rendered_template.encode("UTF-8")), pdf_file, encoding="UTF-8"
        )

        response = HttpResponse(pdf_file.getvalue(), content_type="application/pdf")
        response["Content-Disposition"] = 'attachment; filename="schema.pdf"'

        return response
