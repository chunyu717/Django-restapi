from django.db import models

# Create your models here.
class Language(models.Model):
	name = models.CharField(max_length=50)
	paradigm = models.CharField(max_length=50)

    #def __str__(self):
    #    return self.name
