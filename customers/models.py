from django.db import models
from django.contrib.auth.models import User
import uuid

from famers.models import Product



class Bookmark(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    complete = models.BooleanField(default=False)

    def __str__(self) -> str:
        return str(self.id)

    @property
    def total_price(self):
        bookmarkitems = self.bookmarkitems.all()
        total_cost = sum([item.price for item in bookmarkitems])
        return total_cost

    @property
    def total_items(self):
        bookmarkitems = self.bookmarkitems.all()
        quantity = sum([item.quantity for item in bookmarkitems])
        return quantity


class BookmarkItems(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    bookmark = models.ForeignKey(
        Bookmark, on_delete=models.CASCADE, related_name="bookmarkitems")
    quantity = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = "Bookmark Items"

    def __str__(self) -> str:
        return self.product.title

    @property
    def price(self):
        actual_price = self.product.price*self.quantity
        return actual_price