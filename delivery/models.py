from django.db import models
import uuid



class Types(models.Model):
    title = models.CharField(verbose_name="Тип товара", max_length=64)

    class Meta:
        verbose_name = "Тип товара"
        verbose_name_plural = "Типы товаров"

    def __str__(self):
        return self.title


class Addreses(models.Model):
    name = models.CharField(verbose_name="Адрес доставки", max_length=255)

    class Meta:
        verbose_name = "Адрес доставки"
        verbose_name_plural = "Адреса доставки"

    def __str__(self):
        return self.name


class Products(models.Model):
    title = models.CharField(verbose_name="Название товара", max_length=255)
    product_type = models.ForeignKey(Types, on_delete=models.SET_NULL, verbose_name="Тип товара", null=True)
    delivery_date = models.DateField(verbose_name="Дата доставки")
    file_attachment = models.FileField("Файл", upload_to='media/files')
    address = models.ForeignKey(Addreses,on_delete=models.SET_NULL, verbose_name="Адрес пункта выдачи", null=True)

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
        

    def __str__(self):
        return "%s, %s, %s" % (self.title, self.delivery_date, self.address)