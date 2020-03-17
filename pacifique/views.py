from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import NewArticleForm, UpdateArticleForm
from .models import Article

# pagination
from django.core.paginator import Paginator

# Create your views here.
def home(request):
    articles = Article.objects.all().order_by('-pub_date')[:3]   
    return render(request, 'main/home.html', {"articles": articles})

def articles(request):
    articles_list = Article.objects.all()
    paginator = Paginator(articles_list, 3) # Show 25 contacts per page.

    page_number = request.GET.get('page')
    articles = paginator.get_page(page_number)
    
    return render(request, 'main/articles.html', {"articles": articles})


def article_display(request, article_id):
    try:
        article = Article.objects.get(id=article_id)
    except Article.DoesNotExist:
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


@login_required(login_url='login/')
def update_article(request, article_id):
    current_user=request.user
    if request.method =='POST':
        if Article.objects.filter(id=article_id).exists():
            form = NewArticleForm(request.POST, request.FILES, instance=Article.objects.get(id=article_id))
            if form.is_valid():
                article = form.save(commit=False)
                article.editor = current_user
                article.save()
                print('hellooooooooooooha' + article.title)
            return redirect('articles')
            

    else:
        if Article.objects.filter(id = article_id).exists():
            form = NewArticleForm(instance=Article.objects.get(id=article_id))
            article = Article.objects.get(id=article_id)
            # print('helloooooooooooo' + article.title)
        
    return render(request,'main/update_article.html',{"form":form, "article_id":article_id})


def contact(request):
    return render(request, 'main/contact.html')