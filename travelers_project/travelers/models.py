from django.db import models
from django.contrib.auth.models import User

from geography.models import City
from geography.models import Sight


class Source(models.Model):
    link = models.CharField(max_length=255,
                            default='',
                            blank=False,
                            unique=True,
                            db_index=True,
                            verbose_name='Ссылка')

    class Meta:
        verbose_name = 'Источник'
        verbose_name_plural = 'Источники'
        # db_table = 'sources'


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
    sourses = models.ManyToManyField(Source, verbose_name='Источники')

    class Meta:
        verbose_name = 'Путешественник'
        verbose_name_plural = 'Путешественники'
        # db_table = 'travelers'


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
                              on_delete=models.DO_NOTHING,
                              verbose_name='Достопримечательность')

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        # db_table = 'posts'


class PostPhoto(models.Model):
    photo = models.ImageField(default='',
                              blank=False,
                              upload_to='images/photo/',
                              verbose_name='Изображение')
    post = models.ForeignKey(Post,
                             blank=False,
                             null=False,
                             on_delete=models.CASCADE,
                             verbose_name='Пост')

    class Meta:
        verbose_name = 'Фотография отзыва'
        verbose_name_plural = 'Фотографии отзыва'
        # db_table = 'post_photos'


class Tag(models.Model):
    tag = models.CharField(max_length=50,
                           default='',
                           blank=False,
                           null=False,
                           verbose_name='Тэг')
    post = models.ManyToManyField(Post,
                                  verbose_name='Посты')

    class Meta:
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'
        # db_table = 'tags'


class Travel(models.Model):
    title = models.CharField(max_length=255,
                             default='',
                             verbose_name='Название', )
    slug = models.SlugField(max_length=255,
                            blank=False,
                            db_index=True,
                            verbose_name='Слаг', )
    tag = models.CharField(max_length=255,
                           default='',
                           blank=True,
                           verbose_name='Тэг')
    travelers = models.ManyToManyField(Traveler, verbose_name='Путешественники')
    sourses = models.ManyToManyField(Source, verbose_name='Источники')
    photo = models.CharField(max_length=255,
                             default='',
                             verbose_name='Фото')
    city = models.CharField(max_length=255,
                            default='',
                            blank=False,
                            verbose_name='Город')

    class Meta:
        verbose_name = 'Путешествие'
        verbose_name_plural = 'Путешествия'
        # db_table = 'travels'


class Route(models.Model):
    places = models.ManyToManyField(Sight,
                                    blank=False,
                                    verbose_name='Места')
    user = models.ForeignKey(User,
                             blank=True,
                             null=True,
                             on_delete=models.CASCADE,
                             verbose_name='Пользователь')

    posted = models.BooleanField(default=False, verbose_name='Опубликовано')
    city = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name='Город')

    class Meta:
        verbose_name = 'Маршрут'
        verbose_name_plural = 'Маршруты'
        # db_table = 'routes'
