from django.db import models

# Create your models here.

class Tag(models.Model):
  name =models.CharField(max_length=50)
  
class Category(models.Model):
  name =models.CharField(max_length=200)
  

class Trending(models.Model):
    image = models.ImageField(upload_to='thumbnail')
    article = models.TextField()
    publication_date = models.DateField(auto_now_add=True)
    title = models.CharField(max_length=200)
    
  
class Featured_News(models.Model):
    image = models.ImageField(upload_to='thumbnail')
    article = models.TextField()
    publication_date = models.DateField(auto_now_add=True)
    title = models.CharField(max_length=200)
    
    
class News_Slide(models.Model):
    image = models.ImageField(upload_to='thumbnail')
    article = models.TextField()
    publication_date = models.DateField(auto_now_add=True)
    title = models.CharField(max_length=200)
  
class News_details(models.Model):
    image = models.ImageField(upload_to='thumbnail')
    article = models.TextField()
    publication_date = models.DateField(auto_now_add=True)
    title = models.CharField(max_length=200)
    details = models.TextField()
    sub_title = models.CharField(max_length=200)
    sub_image = models.ImageField(upload_to='thumbnail', null=True)
    sub_details= models.TextField(null=True)
    third_title = models.CharField(max_length=200, null=True)
    third_image = models.ImageField(upload_to='thumbnail', null=True)
    third_details= models.TextField(null=True)
    Tags= models.ManyToManyField(Tag, blank=True)
    category=models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    author = models.CharField(max_length=50)
    views = models.PositiveIntegerField(default=0)
    comment = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title
      

class Comment(models.Model):
    name =models.CharField(max_length=200)
    email=models.EmailField(max_length=100)
    website=models.URLField (max_length=100,default="None", blank=True)
    comment = models.TextField()
    comment_date=models.DateTimeField(null=True, auto_now_add=True)
    image = models.ImageField(upload_to='thumbnail', null=True)
    news_details = models.ForeignKey(News_details, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return self.comment
    
    
class Popular_News(models.Model):
    article = models.TextField()
    publication_date = models.DateField(auto_now_add=True)
    title = models.CharField(max_length=200)
    
    
class Flickr_Photos(models.Model):
    image = models.ImageField(upload_to='thumbnail')
    
      
