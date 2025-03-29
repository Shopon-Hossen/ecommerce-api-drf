from django.contrib.postgres.search import TrigramSimilarity
from shop.models import Shop


def search_shops(query):
    return Shop.objects.annotate(
        similarity=TrigramSimilarity('name', query)
    ).filter(similarity__gt=0.3).order_by('-similarity')
