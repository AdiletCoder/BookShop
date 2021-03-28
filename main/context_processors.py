from .models import Author

def navbar(request):
    authors = Author.objects.all()
    return {'authors': authors}
