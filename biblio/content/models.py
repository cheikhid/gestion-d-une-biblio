from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name


class Book(models.Model):

    x = [
        ("available","available"),
        ("rental","rental"),
        ("sell","sell"),
    ]
    
    title = models.CharField(max_length=50)
    image_book = models.FileField(upload_to='photos', null=True , blank=True)
    author = models.CharField(max_length=50, null=True , blank=True)
    image_author = models.FileField(upload_to='photos', null=True , blank=True)
    page = models.IntegerField(null=True , blank=True)
   # book_type = models.CharField(max_length=10, choices=[('vente', 'Vente'), ('location', 'Location')], default='vente')
    price = models.DecimalField(max_digits=15, decimal_places=2, null=True , blank=True)
    rental_price_day =  models.DecimalField(max_digits=5, decimal_places=2, null=True , blank=True)
    rental_period = models.IntegerField(null=True , blank=True)
    rental_total =  models.DecimalField(max_digits=5, decimal_places=2, null=True , blank=True)
    active = models.BooleanField(default=True)
    status = models.CharField(max_length=50, null=True , blank=True ,default='available', choices=x)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, null=True , blank=True)
    def __str__(self):
        return self.title

