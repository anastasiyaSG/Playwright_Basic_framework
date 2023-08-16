from jinja2 import Environment, FileSystemLoader, TemplateNotFound


def pytest_reporter_render(template_name, dirs, context):
    env = Environment(loader=FileSystemLoader(dirs))
    try:
        template = env.get_template(template_name)
    except TemplateNotFound:
        return
    return template.render(context)

#pytest --html=report_one.html --self-contained-html
