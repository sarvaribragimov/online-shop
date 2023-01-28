from .models.category import Category


def all_categories(request):
    return dict(categories=Category.objects.all())
