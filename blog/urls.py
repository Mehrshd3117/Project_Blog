from django.urls import path
from . import views

# /articles
app_name = "blog"
urlpatterns = [
    path('detail/<slug:slug>', views.ArticleDetailView.as_view(), name="article_detail"),
    path('list', views.ArticleListView.as_view(), name="articles_list"),
    path('category/<int:pk>', views.category_detail, name="category_detail"),
    path('search/', views.search, name="search_articles"),
    path('contactus', views.ContactUsView.as_view(), name="contact_us"),
    path('like/<slug:slug>/<int:pk>', views.like, name="like"),

]



