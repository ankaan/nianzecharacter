from django import template

register = template.Library()

register.filter('any',lambda x: any(x))

@register.tag
def make_list(parser, token):
  """
  Build a list and save it in a variable.

  Taken from: http://stackoverflow.com/questions/3715550/creating-a-list-on-the-fly-in-a-django-template
  By: Will Hardy
  """
  bits = list(token.split_contents())
  if len(bits) >= 4 and bits[-2] == "as":
    varname = bits[-1]
    items = bits[1:-2]
    return MakeListNode(items, varname)
  else:
    raise template.TemplateSyntaxError("%r expected format is 'item [item ...] as varname'" % bits[0])

class MakeListNode(template.Node):
  def __init__(self, items, varname):
    self.items = map(template.Variable, items)
    self.varname = varname

  def render(self, context):
    context[self.varname] = [ i.resolve(context) for i in self.items ]
    return ""
