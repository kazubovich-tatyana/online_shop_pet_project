from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe


@admin.register(AbstractGoods)
class AbstractGoodsAdmin(admin.ModelAdmin):
    fields = ('name', 'slug', 'description', 'type', 'season', 'sex')
    prepopulated_fields = {'slug': ('name', 'sex')}
    list_display = ('id', 'name', 'type', 'season', 'sex', 'slug')
    list_display_links = ('id','type')
    ordering = ('name',)
    list_editable = ('name', 'slug')
    search_fields = ('name',)
    save_on_top = True

@admin.register(ColorCategory)
class ColorCategoryAdmin(admin.ModelAdmin):
    fields = ('color', 'slug', 'image','show_color')
    prepopulated_fields = {'slug': ('color',)}
    list_display = ('id','color', 'show_color')
    ordering = ('color',)
    list_editable = ('color',)
    readonly_fields = ('show_color',)

    @admin.display(description='Фото')
    def show_color(self, color: ColorCategory):
        return mark_safe(f"<img src='{color.image.url}' width = 50px>")


@admin.register(SeasonCategory)
class SeasonCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('season', 'year')}
    list_display = ('id', 'season', 'year', 'slug')
    ordering = ('year',)
    list_editable = ('slug','year', 'season')

@admin.register(SexCategory)
class SexCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('sex',)}
    list_display = ('id', 'sex', 'slug')
    list_editable = ('slug','sex')
    ordering = ('id',)

@admin.register(SizeCategory)
class SizeCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('size',)}
    list_display = ('id', 'size', 'slug')
    ordering = ('size',)
    list_editable = ('slug','size')

@admin.register(TypeCategory)
class TypeCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('type',)}
    list_display = ('id', 'type', 'slug')
    ordering = ('type',)
    list_editable = ('slug','type')
    search_fields = ('type',)

@admin.register(ImagesGoods)
class ImagesGoodsAdmin(admin.ModelAdmin):
    fields = ('goods', 'image', 'show_photo')
    list_display = ('id', 'goods', 'show_photo', 'time_create')
    list_display_links = ('id', 'goods')
    ordering = ('-goods', '-time_create',)
    list_filter = ('goods',)
    search_fields = ('goods',)
    readonly_fields = ('show_photo',)
    list_per_page = 10
    @admin.display(description='Фото')
    def show_photo(self, photo: ImagesGoods):
        return mark_safe(f"<img src='{photo.image.url}' width =50px>")

@admin.register(GoodsCollection)
class GoodsCollectionAdmin(admin.ModelAdmin):
    fields = ('name', 'slug', 'color', 'price', 'new_price', )
    list_display = ('id', 'name', 'slug', 'color','new_model','sale', 'price', 'new_price')
    list_display_links = ('id','name')
    list_editable = ('new_model','sale', 'new_price', 'price')
    ordering = ('name',)
    prepopulated_fields = {'slug': ('name', 'color',)}
    list_per_page = 10
    save_on_top = True


@admin.register(Goods)
class GoodsAdmin(admin.ModelAdmin):
    fields = ('item', 'name', 'slug', 'size', 'quantity',)
    prepopulated_fields = {'slug': ('item', )}
    list_display = ('item', 'name', 'size', 'quantity', 'new_model',)
    list_display_links = ('item','name',)
    ordering = ('-time_update','name',)
    search_fields = ('name__name__name__startswith', 'name__name__type__type__startswith', 'item')
    list_filter = ('name__name__type__type', 'size__size', 'name__color__color')
    save_on_top = True
    list_per_page = 10
    @admin.display(description='Новинка')
    def new_model(self, model:Goods ):
        if model.name.new_model:
            return 'Да'
        return 'Нет'

