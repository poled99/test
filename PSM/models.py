from django.db import models

# Create your models here.
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Employee(BaseModel):
    firstname = models.CharField()
    middlename = models.CharField(null=True, blank=True)
    lastname = models.CharField()
