from django.db import models

class Uploads(models.Model):
    name = models.CharField(max_length=40,blank=True,null=True)
    img_path = models.CharField(max_length=200,blank=True,null=True)

    def __str__(self):
        return self.name 
