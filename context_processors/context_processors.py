from blog.models import Article, Category


def recent_articles(request):
    recent_article = Article.objects.order_by('-created')[:4]
    categories = Category.objects.all()
    return {"recent_article": recent_article, "categories": categories}