from django.views.generic import TemplateView
from vvpages.models import Page


class SitemapRestView(TemplateView):
    template_name = "vvpages/sitemap.html"
    
    def get_context_data(self, **kwargs):
        context = super(SitemapRestView, self).get_context_data(**kwargs)
        root_node, created = Page.objects.get_or_create(url="/")
        if created is True:
            root_node.title = "Home"
            root_node.save()
        nodes = root_node.get_descendants(include_self=True).filter(published=True)
        context['nodes'] = nodes
        return context
