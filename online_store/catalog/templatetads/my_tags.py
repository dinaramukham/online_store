from django import template
register=template.library()
#os.path.abspath(path)
@register.simple_tag
def mediapath(objects):
    return