from django.db import models
from django.contrib.auth.models import User


class Sourse(models.Model):
    link = models.CharField(max_length=255,
                            default='',
                            blank=False,
                            unique=True,
                            db_index=True,
                            verbose_name='Ссылка')

    class Meta:
        verbose_name = 'Источник'
        verbose_name_plural = 'Источники'
        db_table = 'sources'


class TypeOfSights(models.Model):
    title = models.CharField(max_length=255,
                             default='',
                             blank=False,
                             verbose_name='Название')
    time = models.CharField(max_length=100,
                            default='',
                            blank=True,
                            verbose_name='Время')
    colour = models.CharField(max_length=30,
                              default='#0000FF',
                              blank=False,
                              verbose_name='Цвет')
    marker = models.CharField(max_length=30,
                              default='marks/flag-export.png',
                              blank=False,
                              verbose_name='Маркер')

    class Meta:
        verbose_name = 'Тип достопримечательности'
        verbose_name_plural = 'Типы достопримечательностей'
        db_table = 'type_of_sights'


class SectionOfSights(models.Model):
    title = models.CharField(max_length=255,
                             default='',
                             blank=False,
                             verbose_name='Название')
    types = models.ManyToManyField(TypeOfSights,
                                   blank=True,
                                   null=True,
                                   verbose_name='Типы')

    class Meta:
        verbose_name = 'Раздел достопримечательностей'
        verbose_name_plural = 'Разделы достопримечательностей'
        db_table = 'section_of_sights'


class Region(models.Model):
    title = models.CharField(max_length=255,
                             default='',
                             blank=False,
                             verbose_name='Название')
    description = models.TextField(default='',
                                   blank=True,
                                   verbose_name='Описание')

    class Meta:
        verbose_name = 'Регион'
        verbose_name_plural = 'Регионы'
        ordering = ('title',)
        db_table = 'region'

    def __str__(self):
        return self.title


class CityManager(models.Manager):
    def posted(self):
        return self.filter(posted=True)


class City(models.Model):
    title = models.CharField(max_length=255,
                             default='',
                             blank=False,
                             verbose_name='Название')
    description = models.TextField(default='',
                                   blank=True,
                                   verbose_name='Описание')
    slug = models.SlugField(max_length=255,
                            blank=False,
                            db_index=True,
                            verbose_name='Адрес')
    default_zoom = models.PositiveSmallIntegerField(blank=True,
                                                    default=0,
                                                    verbose_name='Масштаб')
    centre_coordinates = models.CharField(max_length=100,
                                          default='',
                                          blank=True,
                                          verbose_name='Координаты')
    posted = models.BooleanField(default=False, verbose_name='Опубликовано')
    show_on_mainmap = models.BooleanField(default=False, verbose_name='Показывать на главной карте')
    regional_center = models.BooleanField(default=True, verbose_name='Региональный центр')
    region = models.ForeignKey(Region,
                               null=True,
                               blank=False,
                               default=None,
                               verbose_name='Регион')
    add_date = models.DateTimeField(null=True,
                                    blank=False,
                                    auto_now_add=True,
                                    verbose_name='Дата добавления')
    last_modified_date = models.DateTimeField(null=True,
                                              blank=False,
                                              auto_now=True,
                                              verbose_name='Дата последнего изменения ')
    autotravel_url = models.CharField(max_length=255,
                                      default='',
                                      blank=True,
                                      verbose_name='URL')
    objects = CityManager()

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'
        ordering = ('title', 'slug')
        db_table = 'cities'

    def __str__(self):
        return self.title


class Sight(models.Model):
    title = models.CharField(max_length=255,
                             default='',
                             blank=False,
                             verbose_name='Название')
    text = models.TextField(default='',
                            blank=False,
                            verbose_name='Описание')
    original_coordinates = models.CharField(max_length=100,
                                            default='',
                                            blank=True,
                                            verbose_name='Оригинальные координаты')
    coordinates = models.CharField(max_length=100,
                                   default='',
                                   blank=True,
                                   verbose_name='Координаты', )
    posted = models.BooleanField(default=False, verbose_name='Опубликовано')
    type = models.ManyToManyField(TypeOfSights,
                                  blank=False,
                                  null=False,
                                  verbose_name='Достопримечательности')
    city = models.ForeignKey(City,
                             blank=True,
                             null=True,
                             verbose_name='Город')
    regional = models.BooleanField(default=False, verbose_name='В регионе')
    price = models.CharField(max_length=100,
                             null=True,
                             blank=True,
                             verbose_name='Цена')
    add_date = models.DateTimeField(null=True,
                                    blank=False,
                                    auto_now_add=True,
                                    verbose_name='Дата добавления')
    fix_date = models.DateTimeField(null=True,
                                    blank=False,
                                    auto_now=True,
                                    verbose_name='Дата исправления')
    address = models.CharField(max_length=255,
                               default='',
                               blank=True,
                               verbose_name='Адрес')
    autotravel_url = models.CharField(max_length=255,
                                      default='',
                                      blank=True,
                                      verbose_name='URL')

    class Meta:
        verbose_name = 'Достопримечательность'
        verbose_name_plural = 'Достопримечтельности'
        db_table = 'sight'

    def __str__(self):
        return self.title


class Traveler(models.Model):
    name = models.CharField(max_length=255,
                            default='',
                            blank=False,
                            verbose_name='Имя')
    link = models.CharField(max_length=255,
                            default='',
                            blank=True,
                            unique=True,
                            verbose_name='Ссылка')
    photo = models.CharField(max_length=255,
                             default='http://gpsnew.ru/images/products/no_picture.jpg',
                             blank=False,
                             verbose_name='Фото')
    sourses = models.ManyToManyField(Sourse,
                                     blank=False,
                                     null=False,
                                     verbose_name='Источники')

    class Meta:
        verbose_name = 'Путешественник'
        verbose_name_plural = 'Путешественники'
        db_table = 'travelers'


class Post(models.Model):
    title = models.CharField(max_length=255,
                             default='',
                             blank=True,
                             verbose_name='Заголовок')
    link = models.CharField(max_length=255,
                            default='',
                            blank=True,
                            db_index=True,
                            verbose_name='Ссылка')
    text = models.TextField(default='',
                            blank=False,
                            verbose_name='Текст')
    coordinates = models.CharField(max_length=100,
                                   default='',
                                   blank=True,
                                   verbose_name='Координаты')
    posted = models.BooleanField(default=False, verbose_name='Опубликовано')
    sight = models.ForeignKey(Sight,
                              blank=True,
                              null=True,
                              verbose_name='Достопримечательность')

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        db_table = 'posts'


class PostPhoto(models.Model):
    photo = models.ImageField(default='',
                              blank=False,
                              upload_to='images/photo/',
                              verbose_name='Изображение')
    post = models.ForeignKey(Post,
                             blank=False,
                             null=False,
                             verbose_name='Пост')

    class Meta:
        verbose_name = 'Фотография отзыва'
        verbose_name_plural = 'Фотографии отзыва'
        db_table = 'post_photos'


class Tag(models.Model):
    tag = models.CharField(max_length=50,
                           default='',
                           blank=False,
                           null=False,
                           verbose_name='Тэг')
    post = models.ManyToManyField(Post,
                                  blank=False,
                                  null=False,
                                  verbose_name='Посты')

    class Meta:
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'
        db_table = 'tags'


class SightPhoto(models.Model):
    photo = models.ImageField(default='',
                              blank=False,
                              upload_to='images/photo/',
                              verbose_name='Изображение')
    sight = models.ForeignKey(Sight,
                              blank=False,
                              null=True,
                              verbose_name='Достпримечательность')
    posted = models.BooleanField(default=True, verbose_name='Опубликовано')

    class Meta:
        verbose_name = 'Фотография достопримечательности'
        verbose_name_plural = 'Фотографии достопримечательности'
        unique_together = ('file', 'sight')
        db_table = 'sight_photos'


class Travel(models.Model):
    title = models.CharField(max_length=255,
                             default='',
                             blank=False,
                             verbose_name='Название', )
    slug = models.SlugField(max_length=255,
                            blank=False,
                            db_index=True,
                            verbose_name='Слаг', )
    tag = models.CharField(max_length=255,
                           default='',
                           blank=True,
                           verbose_name='Тэг')
    travelers = models.ManyToManyField(Traveler,
                                       blank=False,
                                       null=False,
                                       verbose_name='Путешественники')
    sourses = models.ManyToManyField(Sourse,
                                     blank=False,
                                     null=False,
                                     verbose_name='Источники')
    photo = models.CharField(max_length=255,
                             default='',
                             blank=False,
                             verbose_name='Фото')
    city = models.CharField(max_length=255,
                            default='',
                            blank=False,
                            verbose_name='Город')

    class Meta:
        verbose_name = 'Путешествие'
        verbose_name_plural = 'Путешествия'
        db_table = 'travels'


class Route(models.Model):
    places = models.ManyToManyField(Sight,
                                    blank=False,
                                    null=False,
                                    verbose_name='Места')
    user = models.ForeignKey(User,
                             blank=True,
                             null=True,
                             verbose_name='Пользователь')

    posted = models.BooleanField(default=False, verbose_name='Опубликовано')
    city = models.ForeignKey(City, blank=False, null=False, verbose_name='Город')

    class Meta:
        verbose_name = 'Маршрут'
        verbose_name_plural = 'Маршруты'
        db_table = 'routes'


class PopularSight(models.Model):
    sight = models.ForeignKey(Sight,
                              blank=False,
                              default='',
                              verbose_name='Популярные достопримечательности')
    start = models.DateTimeField(auto_now_add=True, verbose_name='Время начала')
    finish = models.DateTimeField(auto_now_add=True, verbose_name='Время окончания')

    class Meta:
        verbose_name = 'Популярная достопримечательность'
        verbose_name_plural = 'Популярные достопримечательности'
        db_table = 'popular_sights'


class PopularRoutes(models.Model):
    sight = models.ForeignKey(Route,
                              blank=False,
                              default='',
                              verbose_name='Популярные маршруты')
    start = models.DateTimeField(auto_now_add=True, verbose_name='Время начала')
    finish = models.DateTimeField(auto_now_add=True, verbose_name='Время окончания')

    class Meta:
        verbose_name = 'Популярный маршрут'
        verbose_name_plural = 'Популярные маршруты'
        db_table = 'popular_routes'
