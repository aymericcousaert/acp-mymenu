from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Category(models.Model):
    name = models.CharField(verbose_name=u"Nombre", max_length=30, blank=False, null=False)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(verbose_name=u"Nombre", max_length=30, blank=False, null=False)
    description = models.TextField(verbose_name=u'Descripción', max_length=500, blank=False, null=False)
    price = models.DecimalField(verbose_name=u'Precio', decimal_places=2, max_digits=6)
    suitForVegetarian = models.BooleanField(verbose_name=u'Apto para Vegetarianos', default=False)
    suitForGlutenIntolerant = models.BooleanField(verbose_name=u'Apto para Celíacos', default=False)
    category = models.ForeignKey(Category, verbose_name="Categoría", on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to="products", verbose_name="Imagen", null=True, blank=True)

    def __str__(self):
        return self.name


class PaymentMethod(models.Model):
    CASH = 'CA'
    CREDIT = 'CC'
    DEBIT = 'DB'

    TYPES = [
        (CASH, 'Efectivo'),
        (CREDIT, 'Crédito'),
        (DEBIT, 'Débito'),
    ]

    description = models.CharField(verbose_name="Descripción", max_length=200, blank=False, null=False)
    payment_type = models.CharField(verbose_name="Tipo de pago", max_length=2, choices=TYPES, blank=False, null=False)

    def __str__(self):
        return self.description


class DailySpecialManager(models.Manager):
    def get_queryset(self):
        specials = super(DailySpecialManager, self).get_queryset()

        for special in specials:
            special.product.discountPrice = "{0:.2f}".format(
                float(special.product.price) * (1 - special.discount / 100))

        return specials


class DailySpecial(models.Model):
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
    discount = models.FloatField(verbose_name="Descuento (%)", blank=False, null=False,
                                 validators=[MinValueValidator(0), MaxValueValidator(99)], default=0)

    objects = DailySpecialManager()

    def __str__(self):
        return "{}: {}".format(self.get_type_display(), self.product)


class Promotion(models.Model):
    description = models.CharField(verbose_name="Descripción", max_length=400, blank=False, null=False)

    def __str__(self):
        return self.description


class Client(models.Model):
    name = models.CharField(verbose_name="Nombre", max_length=30, blank=False, null=False)
    email = models.CharField(primary_key=True, verbose_name="Mail", max_length=50, blank=False, null=False)
    token = models.CharField(verbose_name="token", max_length=20, default=None, blank=True)

    def __str__(self):
        return self.email


class Suggestion(models.Model):
    client = models.ForeignKey(Client, verbose_name="Cliente", on_delete=models.CASCADE)
    description = models.CharField(verbose_name="Descripción", max_length=500, blank=False)

    def __str__(self):
        return "{}: {}".format(self.client.name, self.description)
