from django.views.generic.base import TemplateView

# Create your views here.


class IndexView(TemplateView):
    template_name = "index.html"


index_page = IndexView.as_view()
