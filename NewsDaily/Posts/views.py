from django.core.paginator import Paginator
from django.shortcuts import render
from Posts.models import Post

# Create your views here.


def index(request):
    title = 'Главная страница'
    posts = Post.objects.all().order_by('-public_date')
    article_count = request.POST.get('articleCount', 3)
    paginator = Paginator(posts, article_count)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # Для отладки. После отладки удалить!
    ###########################
    print(f'Paginator = {paginator}')
    print(f'page_number = {page_number}')
    print(f'page_obj = {page_obj}')



    ###########################

    #return render(request, 'index.html', {'posts': posts})
    return render(request, 'index.html', {'page_obj': page_obj})