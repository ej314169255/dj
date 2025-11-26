from django.db import models

# Create your models here.
class Phone(models.Model):
    # TODO: Добавьте требуемые поля
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.IntegerField()
    image = models.ImageField(upload_to="products")

    def __str__(self):
        return self.name