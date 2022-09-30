from django.db import models


class Order(models.Model):
    id = models.IntegerField(
        verbose_name="Порядковый номер заказа", primary_key=True, unique=True
    )
    order_id = models.IntegerField(verbose_name="ID заказа", unique=True)
    price_usd = models.DecimalField(
        verbose_name="Стоимость в $", decimal_places=2, max_digits=15
    )
    price_rub = models.DecimalField(
        verbose_name="Стоимость в рублях",
        null=True,
        blank=True,
        decimal_places=2,
        max_digits=15,
    )
    delivery_date = models.DateField(verbose_name="Срок поставки")

    class Meta:
        ordering = ("id",)
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"
