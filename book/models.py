from datetime import datetime

from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название")
    author = models.CharField(max_length=100, verbose_name="Автор")
    pages = models.IntegerField(verbose_name="Количество страниц")
    description = models.TextField(verbose_name="Описание")
    published_date = models.DateField(verbose_name="Дата публикации")

    def __str__(self):
        return self.title

    class Meta:
        db_table = "book"
        verbose_name = "Книга"
        verbose_name_plural = "Книги"
