from .models import Category

def category_renderer(request):

    return {'category': Category.objects.all() }
