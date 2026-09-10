from django import template
from goods.models import SexCategory, SeasonCategory, TypeCategory

register = template.Library()

@register.inclusion_tag('goods/main_menu.html')
def create_main_menu():

    sex_podcat = SexCategory.objects.all()
    sex_podcat = [{'name': i.sex, 'slug': i.slug} for i in sex_podcat]
    season_podcat = SeasonCategory.objects.all()
    season_podcat = [{'name': i.season +' ' + str(i.year), 'slug': i.slug} for i in season_podcat]
    type_podcat = TypeCategory.objects.all()
    type_podcat = [{'name': i.type, 'slug': i.slug} for i in  type_podcat]


    category_dict = [{'name': 'Новинки', 'slug': 'new', 'podcats': []},
                     {'name': 'Распродажа', 'slug': 'sale', 'podcats': []},
                     {'name': 'Для кого', 'slug': 'sex', 'podcats': sex_podcat},
                     {'name':'Сезон', 'slug':'season','podcats':season_podcat},
                     {'name':'Тип изделия', 'slug':'type','podcats':type_podcat},]
    return {'category_dict':category_dict}
