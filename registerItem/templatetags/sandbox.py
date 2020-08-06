from django import template
from registerItem.models import Stock
from django.db.models import Count

register = template.Library()

@register.simple_tag
def counting_stock_per_category(category):
    stock = Stock.objects.all().filter(category__name=category).aggregate(total_number=Count('name'))['total_number']
    print(stock)
    return stock