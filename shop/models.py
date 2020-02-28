from django.db import models
from django.urls import reverse


# Category Model


class Category(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='category', blank=True)

    # Meta class
    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    # Getting Category
    def get_url(self):
        return reverse('shop:products_by_category', args=[self.slug])


    # Redering Function
    def __str__(self):
        return '{}'.format(self.name)


# Products Model

class Product(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    description = models.TextField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='product', blank=True)
    stock = models.IntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    # Meta Class

    class Meta:
        ordering = ('name',)
        verbose_name = 'product'
        verbose_name_plural = 'products'

    # Getting Reverse Url for Product

    def get_url(self):
        return reverse('shop:ProdCatDetail', args=[self.category.slug, self.slug])

    # Rendering Function

    def __str__(self):
        return '{}'.format(self.name)
