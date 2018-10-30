from django.db import models
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField


class Category(models.Model):
    name = models.CharField('Название', max_length=255, default='')

    def __str__(self):
        return self.name


class News(models.Model):
    category = models.ForeignKey(
        Category,
        verbose_name='Категория',
        related_name='news',
        on_delete=models.CASCADE
    )
    title = models.CharField('Заголовок', max_length=255, default='')
    text = RichTextUploadingField('Текст', max_length=100000, default='')
    image = models.ImageField('Фото', upload_to='images/')
    pub_date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-pub_date']
