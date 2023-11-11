from django.db import models
from django.conf import settings
from sorl.thumbnail import ImageField
from django.shortcuts import reverse, redirect

class Item(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    image = ImageField(upload_to='commerce', blank=True)
    description = models.TextField(max_length=250, default="item description in here")
    slug = models.SlugField()

    def __str__(self):
        return self.title

    def get_absolute_urls(self):
        return reverse("ecommerce:product", kwargs={
            'slug': self.slug
        })

    def get_add_to_cart_url(self):
        return reverse("ecommerce:add_to_cart", kwargs={
            'slug':self.slug
        })

    def get_remove_from_cart_url(self):
        return reverse("ecommerce:remove_from_cart", kwargs={
            'slug':self.slug
        })

class OrderItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                            on_delete=models.CASCADE, blank=True, null=True)
    ordered = models.BooleanField(default=False)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def get_total_price(self):
        return self.quantity * Item.price

    def __str__(self):
        return f"{self.quantity} of {self.item.title}"

class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                              on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)
    order_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)



    def __str__(self):
        return self.user.username


