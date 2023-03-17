from django.views.generic import ListView
from django.shortcuts import render
from articles.models import Article


def articles_list(request):
    template = 'articles/news.html'
    articles = Article.objects.all().order_by('-published_at')

    context = {
        'object_lis': articles,
        }
    return render(request, template, context)






# class ArticlesHome(ListView):
#     articles = Article
#     def articles_list(self, request):
#         template = 'articles/news.html'
#         context = {'articles': self.articles
#
#         }
#         return render(request, template, context)
#     class Meta:
#         ordering = '-published_at'