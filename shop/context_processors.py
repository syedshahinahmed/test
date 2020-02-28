from .models import Category

# Enabling Links across the site


def menu_links(request):
    links = Category.objects.all()
    return dict(links=links)
