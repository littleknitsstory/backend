import json
import tempfile
import uuid
from pathlib import Path

import openai
import pdfkit
from celery import shared_task
from decouple import config
from jinja2 import Template

openai.api_key = config("OPENAI_API_KEY", "OPENAI_API_KEY")
OPENAI_MODEL = config("OPENAI_MODEL", "gpt-3.5-turbo")


def generate_pdf_from_json(json_file, template_file):
    with tempfile.TemporaryDirectory(dir=Path.cwd()) as tmpdirname:
        file_path = f"{tmpdirname}/{uuid.uuid4()}.pdf"

        with open(json_file) as f:
            data = json.load(f)

        with open(template_file, "r", encoding="utf-8") as f:
            source_html = f.read()

        template = Template(source_html)

        options = {
            "encoding": "UTF-8",
        }

        config = pdfkit.configuration(wkhtmltopdf="/usr/local/bin/wkhtmltopdf")
        pdfkit.from_string(
            template.render(data=data),
            file_path,
            configuration=config,
            options=options,
        )
        return file_path


@shared_task
def fetch_data_from_api(prompt):
    completion = openai.ChatCompletion.create(
        model=OPENAI_MODEL, messages=[{"role": "user", "content": f"{prompt}"}]
    )
    return completion
