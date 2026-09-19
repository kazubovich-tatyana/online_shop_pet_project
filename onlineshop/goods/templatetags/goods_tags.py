from django import template
from goods.models import SexCategory, SeasonCategory, TypeCategory

register = template.Library()

@register.inclusion_tag('goods/main_menu.html')
def create_main_menu()->dict:

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

@register.simple_tag
def get_category_dict()->list[dict]:
    category_dict = [{'name': 'Новинки', 'slug': 'new'},
                     {'name': 'Распродажа', 'slug': 'sale'},
                     {'name': 'Для кого', 'slug': 'sex'},
                     {'name': 'Сезон', 'slug': 'season'},
                     {'name': 'Тип изделия', 'slug': 'type'}]
    return category_dict

@register.simple_tag
def get_secondary_footer_menu()->dict:
    secondary_menu = [{'name': 'Доставка и оплата', 'url_name':'delivery_inf'},
                      {'name': 'Возврат и обмен', 'url_name':'exchange_inf'},
                      {'name': 'Публичная оферта', 'url_name':'publish_oferta'},
                      {'name': 'Контакты', 'url_name':'contacts'}]
    return secondary_menu
