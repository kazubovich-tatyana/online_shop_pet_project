from .models import Goods, GoodsCollection, ImagesGoods, AbstractGoods

class GoodsFilterService:
    def __init__(self, **kwargs):
        self.new_goods = []
        self.sale_goods = []
        self.men_goods = []
        self.women_goods = []

    def create_collect_dict(self,goods):
        collect_photo = []
        for i in goods:
            photo = ImagesGoods.objects.filter(goods__id=i.id, represent_photo=True).order_by('-time_create')
            if len(photo) > 0:
                collect_photo.append(photo[0])
            else:
                collect_photo.append(ImagesGoods.objects.filter(goods__id=i.id).order_by('-time_create')[0])
            collect_goods = [{'object': obj, 'photo': photo} for obj, photo in zip(goods, collect_photo)]
        return collect_goods

    def create_collect_goods(self, new_sale=True, **kwargs):
        if new_sale:
            collect = GoodsCollection.objects.filter(**kwargs).values('name').distinct()[:4]
            collect = [GoodsCollection.objects.filter(name=i['name']).filter(**kwargs).order_by('-time_update')[0]
                           for i in collect]
        else:
            collect = AbstractGoods.objects.filter(**kwargs)[:4]
            collect = [GoodsCollection.objects.filter(name__id = i.id).order_by('-time_update')[0] for i in collect]
        return collect

    def get_context(self):
        collect_new = self.create_collect_goods(new_model = True)
        self.new_goods = self.create_collect_dict(collect_new)

        collect_sale = self.create_collect_goods(sale=True)
        self.sale_goods = self.create_collect_dict(collect_sale)

        collect_women = self.create_collect_goods(new_sale = False, sex = 2)
        self.women_goods = self.create_collect_dict(collect_women)

        collect_men = self.create_collect_goods(new_sale = False, sex = 1)
        self.men_goods = self.create_collect_dict(collect_men)

        return ({'new_goods': self.new_goods,
        'new_gallery_container':"gallery_container_" + str(len(self.new_goods)),
        'sale_goods': self.sale_goods,
        'sale_gallery_container': 'gallery_container_' + str(len(self.sale_goods)),
        'women_goods': self.women_goods,
        'women_gallery_container': 'gallery_container_' + str(len(self.women_goods)),
        'men_goods': self.men_goods,
        'men_gallery_container': 'gallery_container_' + str(len(self.men_goods))})
