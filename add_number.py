from behave import given, when, then
from calculator import add

@given(u'Calculator app is run')
def step_impl(context):
    print(u'Step: Given Calculator app is run')

@when(u'I input "{a}" and "{b}" to calculator')
def step_impl(context, a, b):
    print(u'Step: When I input "{}" and "{}" to calculator'. format(a, b))
    context.result = add(a, b)
    print(u'Stored result "{}" in context'. format(context.result))

@then(u'I get result "{out}"')
def step_impl(context, out):
    if (context.result == int(out)):
        print(u'Step: Then I get right result "{}", "{}"'.format(context.result, out))
        pass
    else :
        raise Exception ("Invalid sum is returned.")
