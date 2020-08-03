from django.shortcuts import render, get_object_or_404
from .models import Post
from .forms import EmailPostForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView

# Create your views here.'


def post_list(request):
    object_list = Post.objects.all()
    paginator = Paginator(object_list, 3)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page variable won't be integer,
        # then will be present first page
        posts = paginator.page(1)
    except EmptyPage:
        # If page variable will have higher value than page last number,
        # we will present last page of results
        posts = paginator.page(paginator.num_pages)

    return render(request,
                  'blog/post/list.html',
                  {'page': page,
                   'posts': posts})


def post_detail(request, day, month, year, post):
    post = get_object_or_404(Post, slug=post,
                             status='published',
                             publish__day=day,
                             publish__month=month,
                             publish__year=year)
    return render(request,
                  'blog/post/detail.html',
                  {'post': post})


def post_share(request, post_id):
    # We take a post based on his id
    post = get_object_or_404(Post, id=post_id, status='published')

    if request.method == 'POST':
        # Form was sent.
        form = EmailPostForm(request.POST)
        if form.is_valid():
            # Simply built-in validation
            cd = form.cleaned_data
    else:
        # if GET (empty form), we create new form
        form = EmailPostForm()

    return render(request, 'blog/post/share.html', {
        'post': post,
        'form': form
    })



# Generic view instead simply post view
class PostListView(ListView):
    model = Post
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog/post/list.html'
