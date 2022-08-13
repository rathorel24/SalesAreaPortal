from django.db import models

# Create your models here.

class DivOffice(models.Model):
    id = models.IntegerField(primary_key=True, default=100)
    fieldofficer_name = models.CharField(max_length=70)
    FO_email = models.EmailField(max_length=100)

    def __str__(self):
        return self.fieldofficer_name

class RetailOutlets(models.Model):
    code = models.IntegerField(blank=True,primary_key=True,default=0)
    name = models.CharField(max_length=70)
    area = models.CharField(max_length=70)
    sales = models.IntegerField(default=0)
    FO_name = models.ForeignKey(DivOffice, on_delete=models.CASCADE, related_name='FO_Name')
    type = models.CharField(max_length=30)



