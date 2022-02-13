from django.db import models
# Create your models here.
from django.contrib.auth.models import User


class Applications(models.Model):
    #username password FirstName from User model.
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    contact_no = models.IntegerField(default=0)
    type = models.CharField(max_length=10, null=False, choices=(("JobGiver", "JG"), ("JobSeeker", "JS")))

class WorkType(models.Model):
    TypeOfWork = models.CharField(max_length=50, null=False)
    def __str__(self):
        return self.TypeOfWork

class Work(models.Model):
    work_id = models.ForeignKey(WorkType, null=False, on_delete=models.CASCADE) # one to many relation
    Hours = models.IntegerField(default=0)
    Description = models.CharField(max_length=200, null= False)
    Wages = models.IntegerField(default=0)
    Count = models.IntegerField(default=0) # number of applications.
    city = models.CharField(max_length=255) # extend .
