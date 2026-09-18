from django.views.generic import ListView

from .models import Categories, GoodsCollection, ImagesGoods
from goods.services.services_home_page import GoodsFilterService
from goods.services.services_category_page import CategoryFilterService


class HomePage(ListView):
    model = GoodsCollection
    template_name = 'goods/index.html'
    title = 'Главная страница'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.title
        goods_filter_service = GoodsFilterService()
        context.update(goods_filter_service.get_context())
        return context



class SaleNewCategoryPage(ListView):
    model = GoodsCollection
    template_name = 'goods/category.html'
    title = "Товары по категориям"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category = Categories.objects.get(slug=self.kwargs['cat_slug'])
        context.update(CategoryFilterService(category).get_collect_dict())
        return context





