from django.views.generic import TemplateView
from blog.models import Post
from projects.models import Project

class HomePageView(TemplateView):
    template_name = "pages/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Últimos 3 artículos publicados
        context['latest_posts'] = Post.objects.filter(status='published').order_by('-published_at')[:3]
        
        # Artículo destacado (si existe)
        context['featured_post'] = Post.objects.filter(featured=True, status='published').order_by('-published_at').first()
        
        # 4 Proyectos activos ordenados por el campo order
        context['active_projects'] = Project.objects.filter(active=True).order_by('order')[:4]
        
        return context
