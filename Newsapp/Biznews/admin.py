from django.contrib import admin
from .models import News_details, Tag, Category, Comment,Trending,Featured_News,News_Slide,Flickr_Photos, Popular_News 

# Register your models here.

admin.site.register(News_details)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Comment)
admin.site.register(Trending)
admin.site.register(Featured_News)
admin.site.register(News_Slide)
admin.site.register(Flickr_Photos)
admin.site.register(Popular_News)