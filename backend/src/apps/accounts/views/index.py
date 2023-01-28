from django.views.generic.base import TemplateView

# Create your views here.


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self):
        context = super().get_context_data()
        context["title"] = "Home"
        return context


index_page = IndexView.as_view()
