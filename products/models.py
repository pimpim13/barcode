from django.db import models
import barcode
from barcode.writer import ImageWriter
from io import BytesIO
from django.core.files import File
from django.core.validators import RegexValidator
from barcode_gen import settings
import os


class Product(models.Model):
    name = models.CharField(max_length=200)
    barcode = models.ImageField(upload_to='images/', blank=True)
    country_id = models.CharField(max_length=1, validators=[RegexValidator(regex="[0-9]{1}",
                                  message="Le code pays doit être un chiffre")], default=3, null=True)
    manufacturer_id = models.CharField(max_length=6, validators=[RegexValidator(regex="[0-9]{6}",
                                       message="Le code produit doit être un nombre à 5 chiffres")],
                                       null=True)
    number_id = models.CharField(max_length=5,
                                 validators=[RegexValidator(regex="[0-9]{5}", message="Le code produit doit être un nombre à 5 chiffres")],
                                 null=True)

    def __str__(self):
        return str(self.name)

    def save(self, *args, **kwargs):
        EAN = barcode.get_barcode_class('ean13')
        ean = EAN(f'{self.country_id}{self.manufacturer_id}{self.number_id}', writer=ImageWriter())
        buffer = BytesIO()
        ean.write(buffer)
        self.barcode.save(f"{self.name}_barcode.png", File(buffer), save=False)

        return super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        os.remove(settings.MEDIA_ROOT / str(self.barcode))
        return super(Product, self).delete(*args, **kwargs)

