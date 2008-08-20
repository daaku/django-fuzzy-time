from django import template
from bisect import bisect

register = template.Library()

@register.filter
def fuzzy_time(time):
    """
    Formats a time as fuzzy periods of the day.
    Accepts a datetime.time or datetime.datetime object.
    """
    periods = ["Early-Morning", "Morning", "Mid-day", \
               "Afternoon", "Evening", "Late-Night"]
    breakpoints = [4, 10, 13, 17, 21]
    try:
        return periods[bisect(breakpoints, time.hour)]
    except AttributeError: # Not a datetime object
        return '' #Fail silently
