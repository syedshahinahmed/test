from django.db import models
from shop.models import Product


# Cart Model

class Cart(models.Model):
    cart_id = models.CharField(max_length=250, blank=True)
    date_added = models.DateField(auto_now=True)

    class Meta:
        db_table = 'ShoppingCart'
        ordering = ['date_added']

    def __str__(self):
        return self.cart_id


# Cart Item Model

class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    active = models.BooleanField(default=True)

    class Meta:
        db_table = 'ShppoingCartItem'

    def sub_total(self):
        return self.product.price * self.quantity

    def __str__(self):
        return self.product
