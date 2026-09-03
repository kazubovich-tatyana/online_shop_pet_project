from .models import Goods, GoodsCollection, ImagesGoods, AbstractGoods

class DataMixin:
    title = None
    menu = None
    extra_context = {}
    def __init__(self):
        if self.title:
            self.extra_context['title'] = self.title
        if self.menu:
            self.extra_context['menu'] = self.menu

class CalculateMixin:

    collect_new = GoodsCollection.objects.filter(new_model=True).values('name').distinct()[:4]
    collect_new = [GoodsCollection.objects.filter(new_model=True, name = i['name'])[0] for i in collect_new]
    new_goods = [{'object': i, 'photo': ImagesGoods.objects.filter(goods__id=i.id)[0]} for i in collect_new ]

    collect_sale = GoodsCollection.objects.filter(sale=True).values('name').distinct()[:4]
    print(collect_sale)
    collect_sale = [GoodsCollection.objects.filter(sale=True, name = i['name'])[0] for i in collect_sale]
    sale_goods = [{'object': i, 'photo': ImagesGoods.objects.filter(goods__id=i.id)[0]} for i in collect_sale]

    collect_women = AbstractGoods.objects.filter(sex=2)[:4]
    collect_women = [GoodsCollection.objects.filter(name__id = i.id).order_by('-time_update')[0] for i in collect_women]
    women_goods = [{'object': i, 'photo': ImagesGoods.objects.filter(goods__id=i.id)[0]} for i in collect_women]

    collect_men = AbstractGoods.objects.filter(sex=1)[:4]
    collect_men = [GoodsCollection.objects.filter(name__id = i.id).order_by('-time_update')[0] for i in collect_men]
    men_goods = [{'object': i, 'photo': ImagesGoods.objects.filter(goods__id=i.id)[0]} for i in collect_men]
    title = None
    DataMixin.extra_context.update({'new_goods': new_goods,
        'new_gallery_container':"gallery_container_" + str(len(new_goods)),
        'sale_goods': sale_goods,
        'sale_gallery_container': 'gallery_container_' + str(len(sale_goods)),
        'women_goods': women_goods,
        'women_gallery_container': 'gallery_container_' + str(len(women_goods)),
        'men_goods': men_goods,
        'men_gallery_container': 'gallery_container_' + str(len(men_goods))})

