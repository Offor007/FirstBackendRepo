from django.shortcuts import render, redirect
from .models import News_details, Comment, Tag, Category,Trending,Featured_News,News_Slide 
from .models import Featured_News,News_Slide,Flickr_Photos, Popular_News 
from .forms import ReaderCommentForm 

# Create your views here.

def home_page(request):
  
    news_article = News_details.objects.all()
    trending = Trending.objects.all()
    featured = Featured_News.objects.all()
    slide = News_Slide.objects.all()
    tags = Tag.objects.all()
    cats = Category.objects.all()
    flickr = Flickr_Photos.objects.all()
    popular = Popular_News.objects.all()
    
    context={
      'news_articles': news_article,
      'trending':trending,
      'featured': featured,
      'slides':slide,
      'tags': tags,
       "cats": cats,
       "flickr": flickr,
       "popular": popular,
      
    }
    
    return render(request, 'articles/index.html', context)

def news_detail_view(request, news_id):
    news_articles = News_details.objects.get(id=news_id)
    
    related_news=News_details.objects.filter(category=news_articles.category)
    r_form = ReaderCommentForm()  
    comment = Comment.objects.filter(news_details = news_articles)
    tags = Tag.objects.all()
    cats = Category.objects.all()
    trending = Trending.objects.all()
    flickr = Flickr_Photos.objects.all()
    popular = Popular_News.objects.all()
  
    
    context={
      "news_articles":news_articles,
      "related":related_news,
      "comment_form":r_form,
      "comments": comment,
      'trending':trending,
      'tags': tags,
      "cats": cats,
      "flickr": flickr,
      "popular": popular,
       
    }
  
    return render(request, 'articles/single.html', context)
  
def form_processing(request, news_id):
    if request.method == "POST":
        news_articles = News_details.objects.get(id=news_id)
        form =ReaderCommentForm(request.POST)
        if form.is_valid():
            form_submit=form.save(commit=False)
            form_submit.news_detail=news_articles
            form_submit.save()
        return redirect("news_detail", news_id=news_articles.id)
      


def count(request, news_id):
    news_obj = News_details.objects.get(id=news_id)
    comment_count = news_obj.comment.count()
    return render(request, 'article/single.html', {'comment_count': comment_count})
  

def contact_page(request):
  
  return render(request, 'articles/contact.html')

def category_page(request):
  
  return render(request, 'articles/category.html')