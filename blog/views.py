from django.views.generic import DetailView, ListView
from .models import Post

class ArticleListView(ListView):
    model = Post
    template_name = 'blog/article_list.html'
    context_object_name = 'posts'
    paginate_by = 9

    def get_queryset(self):
        return Post.objects.filter(status='published').order_by('-published_at')

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'blog/article_detail.html'
    context_object_name = 'post'
