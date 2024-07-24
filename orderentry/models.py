from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils import timezone
import uuid

class customerInfo (models.Model):
    class Meta:
        verbose_name = "Customer Information"
        verbose_name_plural = "Customer Information Entries"

    customer_first_name = models.CharField(max_length=30)
    customer_last_name = models.CharField(max_length=30)
    shipping_address = models.CharField(max_length=60)
    billing_address = models.CharField(max_length=60)
    customer_status_choices = [('PREFFERED','preferred'),('OKAY', 'okay'),('SHAKY', 'shaky')]
    customer_status = models.CharField(max_length=30, choices = customer_status_choices, default="PREFERRED")

    def __str__(self):
        return '%s %s' % (self.customer_first_name, self.customer_last_name)

class orderInfo (models.Model):
    class Meta:
        verbose_name = "Order Information"
        verbose_name_plural = "Order Information Entries"
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this invoice')
    order_Item_Flavor = models.ForeignKey('inventory.flavor', on_delete=models.CASCADE, default="Vanilla")
    order_Sizes = models.ForeignKey('inventory.sizes', on_delete=models.CASCADE, default="Pint")
    order_Quantity = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(999)])
    order_Shipping = models.ForeignKey('inventory.shipping', on_delete=models.CASCADE, default="Standard")
    order_Status_Choices = [('PROCESSING', 'Processing'),('SHIPPED', 'Shipped'),('DELIVERED', 'Delivered'),('CANCELED', 'Canceled')]
    order_Status = models.CharField(max_length=30, choices = order_Status_Choices, default="PROCESSING")
    order_Price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    order_Date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return '%s %ss %s' % (self.order_Quantity, self.order_Sizes.size, self.order_Item_Flavor)
    
    def save(self, *args, **kwargs):
        self.order_Price = self.order_Quantity * self.order_Sizes.price + self.order_Shipping.price
        super(orderInfo, self).save(*args, **kwargs)