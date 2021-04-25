from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Asset(models.Model):
    relative_id = models.CharField(
        max_length=8, unique=True, null=True)  # MDX0001
    name = models.CharField(max_length=127)
    manufacturer = models.ForeignKey('Manufacturer',
                                     on_delete=models.SET_NULL,
                                     null=True)  # when manufacturer deleted asset manufacturer will be null
    category = models.ForeignKey('Category',
                                 on_delete=models.SET_NULL,
                                 null=True)
    organization = models.ForeignKey('authz.Organization',
                                     on_delete=models.CASCADE,
                                     null=True)  # if org deleted, all assets will be deleted
    location = models.CharField(max_length=127)
    purchase_date = models.DateField()
    warranty = models.IntegerField(default=0)
    last_repair = models.DateField(null=True)
    asset_user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    physical_address = models.CharField(
        max_length=32, null=True)  # for hardware
    digital_key = models.CharField(max_length=48, null=True)  # for software
    # for status field
    AVAILABLE = "available"
    IN_USE = "in use"
    NEED_MAINTENANCE = "need maintenance"

    STATUS_CHOICES = (
        (AVAILABLE, 'AVAILABLE'),
        (IN_USE, 'IN_USE'),
        (NEED_MAINTENANCE, 'NEED_MAINTENANCE')
    )
    status = models.CharField(choices=STATUS_CHOICES,
                              default=AVAILABLE, max_length=32)
    note = models.TextField(max_length=200, null=True)  # for any comments

    def __str__(self):
        return self.name

    # @property
    # def relative_id(self):
    #     return "A%05d" % self.id


class Category(models.Model):
    name = models.CharField(max_length=127)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"


class Manufacturer(models.Model):
    name = models.CharField(max_length=127)

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=127)
    description = models.TextField(max_length=255)
    label = models.CharField(max_length=15)  # to specify keyword

    def __str__(self):
        return self.name
