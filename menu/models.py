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


class DailySpecialManager(models.Manager):
    def get_queryset(self):
        specials = super(DailySpecialManager, self).get_queryset()
        for special in specials:
            special.product.discountPrice = "{0:.2f}".format(float(special.product.price) * DailySpecial.DISCOUNT)
        return specials


class DailySpecial(models.Model):
    DISCOUNT = 0.85
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

    objects = DailySpecialManager()

    def get(self):
        specials = list(DailySpecial.objects.all())
        for special in specials:
            special.product.price = "{0:.2f}".format(float(special.product.price) * DailySpecial.DISCOUNT)
        return specials


class Promotion(models.Model):
    description = models.CharField(max_length=400, blank=False, null=False)


class Client(models.Model):
    name = models.CharField(verbose_name="Nombre", max_length=30, blank=False, null=False)
    email = models.CharField(primary_key=True, verbose_name="Mail", max_length=50, blank=False, null=False)
    token = models.CharField(verbose_name="token", max_length=20, default=None, blank=True)

    def __str__(self):
        return self.email
