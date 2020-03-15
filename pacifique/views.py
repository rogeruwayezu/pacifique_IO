
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import NewArticleForm
from .models import Article

# pagination
from django.core.paginator import Paginator

# Create your views here.
def home(request):
    return render(request, 'main/home.html')

def articles(request):
    articles_list = Article.objects.all()
    print('hello' + str(len(articles_list)))
    paginator = Paginator(articles_list, 2) # Show 25 contacts per page.

    page_number = request.GET.get('page')
    articles = paginator.get_page(page_number)
    
    return render(request, 'main/articles.html', {"articles": articles})

def article_display(request, article_id):
    try:
        article = Article.objects.get(id=article_id)
    except DoesNotExist:
        raise Http404()
    return render(request, 'main/article_display.html', {"article": article})

@login_required(login_url='/accounts/login/')
def new_article(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.editor = current_user
            article.save()
        return redirect('articles')

    else:
        form = NewArticleForm()
    return render(request, 'main/new_article.html', {"form": form})


def contact(request):
    return render(request, 'main/contact.html')