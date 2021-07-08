from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import News, Comment, Category
from .forms import CommentForm, NewsForm, CategoryForm


# Create your views here.
def index(request):
    category = Category.objects.all()
    news = News.objects.order_by('date_added')
    context = {'cate': category, 'news': news}
    return render(request, "index.html", context)


def category(request, category_id):
    category = Category.objects.get(pk=category_id)
    news = category.news_set.order_by('date_added')
    categoryall = Category.objects.all()
    context = {'cate': categoryall, 'news': news, 'catedetail': category}
    return render(request, "category.html", context)


def detail(request, new_id):
    news = News.objects.get(pk=new_id)
    """Add a new comment."""
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = CommentForm()
    else:
        # POST data submitted; process data.
        form = CommentForm(data=request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.news = news
            form.save()
            return redirect('news:detail', new_id=new_id)

    # Display a blank or invalid form.
    categoryall = Category.objects.all()
    comment = news.comment_set.order_by('date_added')
    context = {'form': form, 'cate': categoryall, 'news': news, 'comment': comment}
    return render(request, 'detail.html', context)


def search(request):
    categoryall = Category.objects.all()
    search_query = request.GET.get('search', '')
    if search_query:
        news = News.objects.filter(title__icontains=search_query)

    context = {'cate': categoryall, 'news': news, 'search': search_query}
    return render(request, 'search.html', context)


def add(request):
    """Add a new News."""
    # No data submitted; create a blank form.
    form_cate = CategoryForm()
    form_news = NewsForm()
    category = Category.objects.all()
    news = News.objects.order_by('date_added')
    context = {'form_news': form_news, 'form_cate': form_cate, 'cate': category, 'news': news}
    return render(request, 'addnews.html', context)


def admin_cate(request, category_id):
    # No data submitted; create a blank form.
    form_cate = CategoryForm()
    form_news = NewsForm()
    category = Category.objects.get(pk=category_id)
    news = category.news_set.order_by('date_added')
    categoryall = Category.objects.all()
    context = {'form_news': form_news, 'form_cate': form_cate, 'cate': categoryall, 'news': news, 'catedetail': category}
    return render(request, "addnews.html", context)


def add_news(request):
    """Add a new News."""
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form_news = NewsForm()
    else:
        # POST data submitted; process data.
        form_news = NewsForm(request.POST, request.FILES)
        if form_news.is_valid():
            form_news.save()
            return redirect('news:add')

    form_cate = CategoryForm()
    category = Category.objects.all()
    news = News.objects.order_by('date_added')
    error_add_news = 'Thêm Danh Mục Thất Bại'
    context = {'form_news': form_news, 'form_cate': form_cate, 'cate': category, 'news': news, 'error_add_news': error_add_news}
    return render(request, 'addnews.html', context)


def add_cate(request):
    """Add a new Category."""
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form_cate = CategoryForm()
    else:
        # POST data submitted; process data.
        form_cate = CategoryForm(data=request.POST)
        if form_cate.is_valid():
            form_cate.save()
            return redirect('news:add')

    form_news = NewsForm()
    category = Category.objects.all()
    news = News.objects.order_by('date_added')
    error_add_cate = 'Thêm Danh Mục Thất Bại'
    context = {'form_news': form_news, 'form_cate': form_cate, 'cate': category, 'news': news, 'error_add_cate': error_add_cate}
    return render(request, 'addnews.html', context)


# delete view for details
def delete_news(request, new_id):
    # fetch the object related to passed id
    obj = get_object_or_404(News, id=new_id)

    if request.method == "POST":
        # delete object
        obj.delete()
        # after deleting redirect to
        # home page
        return redirect('news:add')
    error_delete = 'Xóa Thất Bại'
    # No data submitted; create a blank form.
    form_cate = CategoryForm()
    form_news = NewsForm()
    category = Category.objects.all()
    news = News.objects.order_by('date_added')
    context = {'form_news': form_news, 'form_cate': form_cate, 'cate': category, 'news': news, 'error_delete': error_delete}
    return render(request, "addnews.html", context)


def edit_news(request, new_id):
    # fetch the object related to passed id
    news = get_object_or_404(News, id=new_id)

    if request.method != 'POST':
        # Initial request; pre-fill form with the current entry.
        form_news_edit = NewsForm(instance=news)
    else:
        # POST data submitted; process data.
        form_news_edit = NewsForm(instance=news, data=request.POST)
        if form_news_edit.is_valid():
            form_news_edit.save()
            return redirect('news:add')
    error_edit = 'Sửa Thất Bại'
    # No data submitted; create a blank form.
    form_cate = CategoryForm()
    form_news = NewsForm()
    category = Category.objects.all()
    context = {'form_news': form_news, 'form_cate': form_cate, 'form_news_edit': form_news_edit, 'cate': category, 'news': news, 'error_edit': error_edit}
    return render(request, "editnews.html", context)
