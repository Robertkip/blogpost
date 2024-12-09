from django.shortcuts import render
from .models import Post, Comment
from .forms import SearchForm

# Create your views here.

def blog_index(request):
    posts = Post.objects.all().order_by("created")
    context = {
        "posts": posts,
    }
    return render(request, "core/index.html", {"posts": posts})


def blog_category(request, category):
    posts = Post.objects.filter(
        categories__name__contains = category
    ).order_by("created")
    context = {
        "category": category,
        "posts": posts,
    }
    return render(request, "core/category.html", context)


def blog_detail(request, pk):
    post = Post.objects.get(pk=pk)
    comments = Comment.objects.filter(post=post)
    context = {
        "post": post,
        "comments": comments,
    }

    return render(request, "core/detail.html", context)


def search(request):
    form = SearchForm()
    results = []

    if request.method == "GET" and "query" in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data["query"]
            # Perform a case-insensitive search
            results = Post.objects.filter(title__icontains=query)

    # Always return an HttpResponse object
    return render(request, "core/search.html", context={"form": form, "results": results})