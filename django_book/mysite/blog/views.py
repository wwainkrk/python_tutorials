from django.shortcuts import render, get_object_or_404
from .models import Post, Comment
from .forms import EmailPostForm, CommentForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView
from taggit.models import Tag

# Create your views here.'


def post_list(request, tag_slug=False):
    object_list = Post.objects.all()
    tag = None

    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        object_list = object_list.filter(tags__in=[tag])

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

    return render(request, 'blog/post/list.html', {
        'page': page,
        'posts': posts,
        'tag': tag,
    })


def post_detail(request, day, month, year, post):
    post = get_object_or_404(Post, slug=post,
                             status='published',
                             publish__day=day,
                             publish__month=month,
                             publish__year=year)

    # We are taking all comments with active status as QuerySet
    comments = post.comments.filter(active=True)

    if request.method == "POST":
        # We are filling comment with request data
        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            # We create new comment, False flag mean that we are not save yet new object
            new_comment = comment_form.save(commit=False)
            # We sign new comment to current post
            new_comment.post = post
            # Saving new comment in database
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request, 'blog/post/detail.html', {
        'post': post,
        'comments': comments,
        'comment_form': comment_form
    })


def post_share(request, post_id):
    # We take a post based on his id
    post = get_object_or_404(Post, id=post_id, status='published')
    sent = False

    if request.method == 'POST':
        # Form was sent.
        form = EmailPostForm(request.POST)
        if form.is_valid():
            # Simply built-in validation
            cd = form.cleaned_data
            post_url = request.build_absolute_uri(
                post.get_absolute_url()
            )
            subject = '{} ({}) sent you to read "{}"'.format(cd['name'], cd['email'], post.title)
            message = 'Read a post "{}" on page {}\n\n Comment added by {}: {}'.format(
                post.title, post_url, cd['name'], cd['comments']
            )
            sent = True
    else:
        # if GET (empty form), we create new form
        form = EmailPostForm()

    return render(request, 'blog/post/share.html', {
        'post': post,
        'form': form,
        'sent': sent
    })


# Generic view instead simply post view
class PostListView(ListView):
    model = Post
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog/post/list.html'
