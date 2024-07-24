from django.db import models
from django.core import validators

class sizes (models.Model):
    class Meta:
        verbose_name = "Size"
        verbose_name_plural = "Sizes"

    size = models.CharField (primary_key=True, max_length=30, unique=True, blank=False)
    price = models.DecimalField(default=3.99, decimal_places=2, max_digits= 4)
    

    def __str__(self):
        return '%s ($%s)' % (self.size, self.price)

class flavor (models.Model):
    class Meta:
        verbose_name = "Flavor"
        verbose_name_plural = "Flavors"

    flavor = models.CharField(primary_key=True, max_length=30, unique=True, blank=False)
    
    def __str__(self):
        return '%s' % self.flavor

class shipping (models.Model):
    class Meta:
        verbose_name = "Shipping"
        verbose_name_plural = "Shipping options"

    type = models.CharField (primary_key=True, max_length=30, unique=True, blank=False)
    price = models.DecimalField(default=14.99, decimal_places=2, max_digits= 4)

    def __str__(self):
        return '%s ($%s)' % (self.type, self.price)


