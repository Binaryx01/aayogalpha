from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Post

# Create your views here.

def index(request):
    post = Post.objects.all()
    #for pagination
    paginator = Paginator(post, 5)  # Paginate with 5 posts per page
    page_number = request.GET.get('page')  # Get the current page number
    post = paginator.get_page(page_number)  # Get paginated posts
    return render(request, "aayogkhabarapp/index.html",{'post':post})

