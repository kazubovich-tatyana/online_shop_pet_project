from goods.models import ImagesGoods, GoodsCollection
class CategoryFilterService:
    def __init__(self, category):
        self.category = category

    def _get_goods(self, slug:str)->list[dict]:
        check_values = 'new_model' if slug == 'new' else 'sale'
        posts = GoodsCollection.objects.filter(**{check_values: True}).order_by('-time_update')
        collect_photo = []
        for i in posts:
            photo = ImagesGoods.objects.filter(goods__id=i.id, represent_photo=True).order_by('-time_create')
            if len(photo) > 0:
                collect_photo.append(photo[0])
            else:
                collect_photo.append(ImagesGoods.objects.filter(goods__id=i.id).order_by('-time_create')[0])
        goods = [{'object': posts[i], 'photo': collect_photo[i]} for i in range(len(collect_photo))]
        return goods
    def _get_css_class_name(self, goods:list[dict]) -> str:
        lenght = len(goods) if len(goods) < 4 else 4
        return 'gallery_container_' + str(lenght)

    def get_collect_dict(self)->dict:
        context = {'goods': self._get_goods(self.category.slug),
                   'page_name': self.category.name,
                   'page_slug': self.category.slug
                   }
        context['gallery_container'] = self._get_css_class_name(context['goods'])
        return context
