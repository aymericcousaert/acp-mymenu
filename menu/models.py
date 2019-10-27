from django.db import models


class Category(models.Model):
    name = models.CharField(verbose_name=u"Nombre", max_length=30, blank=False, null=False)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(verbose_name=u"Nombre", max_length=30, blank=False, null=False)
    description = models.TextField(verbose_name=u'Descripcion', max_length=500, blank=False, null=False)
    price = models.DecimalField(verbose_name=u'Precio', decimal_places=2, max_digits=6)
    suitForVegetarian = models.BooleanField(default=False)
    suitForGlutenIntolerant = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name


class PaymentMethod(models.Model):
    CASH = 'CA'
    CREDIT = 'CC'
    DEBIT = 'DB'

    TYPES = [
        (CASH, 'Efectivo'),
        (CREDIT, 'Credito'),
        (DEBIT, 'Debito'),
    ]

    description = models.CharField(max_length=200, blank=False, null=False)
    payment_type = models.CharField(max_length=2, choices=TYPES, blank=False, null=False)

    def __str__(self):
        return self.description


class TodaysMenuDish(models.Model):
    FIRSTPLATE = 'FP'
    MAINPLATE = 'MP'
    DESSERT = 'DE'
    DRINK = 'DK'

    TYPES = [
        (FIRSTPLATE, 'Entrada'),
        (MAINPLATE, 'Plato principal'),
        (DESSERT, 'Postre'),
        (DRINK, 'Bebida'),
    ]

    type = models.CharField(primary_key=True, verbose_name="Tipo", max_length=2, choices=TYPES, blank=False, null=False)
    product = models.ForeignKey(Product, verbose_name='Producto', related_name='product', on_delete=models.CASCADE)
