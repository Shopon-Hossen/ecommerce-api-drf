from django.contrib.postgres.search import TrigramSimilarity


def search(query, model, field):
    return model.objects.annotate(
        similarity=TrigramSimilarity(field, query)
    ).filter(similarity__gt=0.4).order_by('-similarity')
