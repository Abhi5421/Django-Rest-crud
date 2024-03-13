from django.db import models


# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=255)
    subcategory = models.CharField(max_length=255)
    amount = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey('auth.User', related_name='items', on_delete=models.CASCADE, default=1)

    class Meta:
        db_table = 'Item'

    def __str__(self):
        return self.name
