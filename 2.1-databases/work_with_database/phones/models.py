from django.db import models


class Phone(models.Model):
    # TODO: Добавьте требуемые поля
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    price = models.IntegerField(default=5)
    image = models.ImageField(upload_to="product")
    release_date = models.TextField()
    lte_exists = models.BooleanField()
    slug = models.SlugField(max_length=200)

    def __str__(self):
        return self.name