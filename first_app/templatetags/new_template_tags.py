from first_app.models import Person
from django import template

register = template.Library()



@register.inclusion_tag('all_persons.html', takes_context = True )
def all_persons(context):

    # Fetch Data From Person Model
    persons = Person.objects.all()
    context = {
        'persons': persons,
    }
    return context


@register.simple_tag
def male_persons():
    return Person.objects.filter(gender='M').count()
    

@register.filter
def lower(value):
    return value.lower()


@register.filter(name='color')
def get_color(value):

    if value=='Female':
        return "red"
    elif value == 'Male' :
        return "green"
    else:
        return "yellow"


@register.filter(name='custom_filter')
def custom_filter(value):

    if value=='Female':
        return "Girl"
    elif value == 'Male' :
        return "Boy"
    else:
        return "Unknown"







@register.filter('modify_name')
def female_members(value, arg):
    # if arg is first_name: return the first string before space
    if arg == "first_name":
        return value.split("*")[0]
    # if arg is last_name: return the last string before space
    if arg == "last_name":
        return value.split(" ")[-1]
    # if arg is title_case: return the title case of the string
    if arg == "title_case":
        return value.title()
    return value


