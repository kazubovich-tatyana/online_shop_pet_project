from django.db import models

# Create your models here.
class Categories(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        verbose_name = 'Категории'
        verbose_name_plural = 'Категории'
    def __str__(self):
        return self.name

class ColorCategory(models.Model):
    color = models.CharField(max_length=30, verbose_name='Цвет')
    slug = models.SlugField(max_length=50, unique=True, db_index=True)
    image = models.ImageField(upload_to='goods/color/', verbose_name="Фото")
    class Meta:
        verbose_name = 'Цвет'
        verbose_name_plural = 'Цвет'
    def __str__(self):
        return str(self.id)+self.color

class SeasonCategory(models.Model):
    season = models.CharField(max_length=10, verbose_name = 'Сезон')
    year = models.IntegerField(null=True, blank=True, verbose_name = 'Год')
    slug = models.SlugField(max_length=50, unique=True, db_index=True)
    class Meta:
        verbose_name = 'Сезон коллекции'
        verbose_name_plural = 'Сезон коллекции'
    def __str__(self):
        return self.season + ' ' + str(self.year)

class SexCategory(models.Model):
    sex = models.CharField(max_length=10, verbose_name = 'Пол')
    slug = models.SlugField(max_length=50, unique=True, db_index=True)
    class Meta:
        verbose_name = 'Пол'
        verbose_name_plural = 'Пол'
    def __str__(self):
        return str(self.id)+self.sex

class SizeCategory(models.Model):
    size = models.IntegerField(verbose_name='Размер')
    slug = models.SlugField(max_length=50, unique=True, db_index=True)
    class Meta:
        verbose_name = 'Размер'
        verbose_name_plural = 'Размер'
    def __str__(self):
        return str(self.size)

class TypeCategory(models.Model):
    type = models.CharField(max_length=55, verbose_name='Тип')
    slug = models.SlugField(max_length=50, unique=True, db_index=True)
    class Meta:
        verbose_name = 'Тип товара'
        verbose_name_plural = 'Тип товара'
    def __str__(self):
        return str(self.id)+self.type

class AbstractGoods(models.Model):
    name = models.CharField(max_length=100, verbose_name= 'Название')
    slug = models.SlugField(max_length=50, unique=True, db_index=True)
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    type = models.ForeignKey(TypeCategory, on_delete=models.PROTECT, verbose_name='Тип')
    season = models.ForeignKey(SeasonCategory, on_delete=models.PROTECT, verbose_name='Сезон')
    sex = models.ForeignKey(SexCategory, on_delete=models.PROTECT, verbose_name='Пол')
    time_update= models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name = 'Описание товара'
        verbose_name_plural = 'Описание товара'
        ordering = ['-time_update']
        indexes = [models.Index(fields=['-time_update'])]
    def __str__(self):
        return str(self.id)+self.name

class GoodsCollection(models.Model):
    name = models.ForeignKey(AbstractGoods, on_delete=models.PROTECT, verbose_name='Название')
    slug = models.SlugField(max_length=50, unique=True, db_index=True)
    color = models.ForeignKey(ColorCategory, on_delete=models.PROTECT, verbose_name='Цвет')
    new_model = models.BooleanField(default=False, verbose_name='Новинка')
    sale = models.BooleanField(default=False, verbose_name='Распродажа')
    price = models.CharField(max_length=50, null=True, verbose_name='Цена')
    new_price = models.CharField(max_length=50, null=True, blank=True, verbose_name='Новая цена')
    time_update = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name = 'Витрина'
        verbose_name_plural = 'Витрина'
        ordering = ('-time_update',)
        indexes = [models.Index(fields=['time_update'])]
    def __str__(self):
        return str(self.name) + ' ' + str(self.color)


class ImagesGoods(models.Model):
    goods = models.ForeignKey(GoodsCollection, on_delete=models.PROTECT, verbose_name='Товар')
    image = models.ImageField(upload_to='goods/photo', verbose_name="Фото")
    time_create = models.DateTimeField(auto_now_add=True)
    represent_photo = models.BooleanField(default=False, verbose_name='Карточка товара')
    class Meta:
        verbose_name = 'Фото товара'
        verbose_name_plural = 'Фото товара'

class Goods(models.Model):
    item = models.CharField(max_length=50, verbose_name='Артикул')
    name = models.ForeignKey(GoodsCollection, on_delete=models.PROTECT, verbose_name='Название')
    slug = models.SlugField(max_length=50, unique=True, db_index=True)
    size = models.ForeignKey(SizeCategory, on_delete=models.PROTECT, verbose_name='Размер')
    quantity = models.IntegerField(verbose_name='Остаток')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Время изменения')


    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товар'
    def __str__(self):
        return str(self.item) + ' ' + str(self.name)


