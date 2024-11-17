from django.core.paginator import Paginator
from django.shortcuts import render
from Posts.models import Post

# Create your views here.


def index(request):
    title = 'Главная страница'
    posts = Post.objects.all().order_by('-public_date')
    paginator = Paginator(posts, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    
    return render(request, 'index.html', {'page_obj': page_obj})


