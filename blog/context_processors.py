from datetime import datetime
from random import randint

from .models import Category, Tip


def get_categories():
    categories = Category.objects.all()
    return categories


def tips():
    try:
        count = Tip.objects.count()
        tip = Tip.objects.all()[randint(0, count - 1)]
    except ValueError:
        tip = None
    return tip


def constants(request):
    return {
        'year': datetime.now().year,
        'tip': tips(),
        'categories': get_categories(),
    }
