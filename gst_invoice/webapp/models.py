from django.db import models


# Create your models here.
class bill(models.Model):
    item_name = models.CharField(max_length=50, null=False)
    price = models.FloatField(max_length=255, null=False)
    gst_slab = models.FloatField(max_length=5, null=False)


    def _str_(self):
        return self.item_name
        
