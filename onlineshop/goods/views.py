from django.shortcuts import render
from django.views.generic import ListView

from .models import Goods, Categories, GoodsCollection, ImagesGoods

from .utils import CalculateMixin, DataMixin


class HomePage(DataMixin, CalculateMixin, ListView):
    model = GoodsCollection
    template_name = 'goods/index.html'
    title = 'Главная страница'



class SaleNewCategoryPage(ListView):
    model = GoodsCollection
    template_name = 'goods/category.html'
    title = "Товары по категориям"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        content = Categories.objects.get(slug=self.kwargs['cat_slug'])
        context['page_name']= content.name
        context['page_slug']= content.slug
        context['goods'] = self.get_goods(content.slug)
        context['gallery_container'] = self.get_css_class_name(context['goods'])
        return context
    def get_goods(self, slug):
        check_values = 'new_model' if slug == 'new' else 'sale'
        posts = self.model.objects.filter(**{check_values:True}).order_by('-time_update')
        image = [ImagesGoods.objects.filter(goods__id=i.id).order_by('-time_create')[0]
                 if len(ImagesGoods.objects.filter(goods__id=i.id))>0 else None for i in posts]
        goods = [{'object':posts[i], 'photo':image[i]} for i in range(len(image))]
        return goods
    def get_css_class_name(self, goods):
        lenght = str(len(goods)) if len(goods)< 4 else '4'
        return 'gallery_container_' +lenght



