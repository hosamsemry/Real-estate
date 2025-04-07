from django.db import models
from django.conf import settings

    
class Listing(models.Model):

    class SaleType(models.TextChoices):
        FOR_SALE = 'For Sale'
        FOR_RENT = 'For Rent'

    class HomeType(models.TextChoices):
        CONDO = 'Condo'
        HOUSE = 'House'
        TOWNHOUSE = 'Townhouse'

    
    
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=10)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    bedrooms = models.IntegerField()
    bathrooms = models.DecimalField(max_digits=2, decimal_places=1)
    sale_type = models.CharField(
        max_length=10,
        choices=SaleType.choices,
        default=SaleType.FOR_SALE,
    )
    home_type = models.CharField(
        max_length=10,
        choices=HomeType.choices,
        default=HomeType.HOUSE,
    )
    main_photo = models.ImageField(upload_to='listings/')
    photo_1 = models.ImageField(upload_to='listings/', blank=True, null=True)
    photo_2 = models.ImageField(upload_to='listings/', blank=True, null=True)
    photo_3 = models.ImageField(upload_to='listings/', blank=True, null=True)
    is_published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title 
