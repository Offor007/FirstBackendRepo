from django.urls import path
from Biznews.views import home_page, contact_page, news_detail_view, category_page, form_processing

urlpatterns = [
    path('', home_page, name="home"),
    path('single/<int:news_id>/', news_detail_view, name="news_detail"),
    path('process-data/<int:news_id>/', form_processing, name="form_processing"),
    path('contact/', contact_page, name="contact"),
    path('category/', category_page, name="category"),
    ]