import json
import tempfile
import uuid
from pathlib import Path

import pdfkit
from jinja2 import Template


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
