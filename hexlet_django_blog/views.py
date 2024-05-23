from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        return {'who': 'World'}



class AboutView(TemplateView):
    template_name = 'about.html'
