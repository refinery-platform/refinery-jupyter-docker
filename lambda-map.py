import re

template = '&facet.field={0}_Characteristics_generic_s&facet.field={0}_Factor_Value_generic_s'
old = ''.join(
    map(lambda s: template.format(s, s),
        re.split(r'\s*,\s*', "dog,cat,bird"))
)

new = ''.join([template.format(s) for s in "dog,cat,bird".split(",")])

assert old == new, "{} != {}".format(old, new)

print new
