import os
from core.conf import settings


def get_template_path(template_name):
    return os.path.join(settings.TEMPLATE_DIR, template_name)


def render_template(template_name, context=None):
    context = context or dict()
    with open(get_template_path(template_name)) as template:
        return template.read()
