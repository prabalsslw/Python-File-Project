import os
from django.db import models
from django.http import HttpResponse

class Profile(models.Model):
    GENDER_CHOICES = (
        ("Male", "Male"),
        ("Female", "Female"),
        ("Other", "Other"),
    )
    fullname = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phone = models.CharField(max_length=11)
    gender = models.CharField(max_length=15, choices = GENDER_CHOICES)
    about = models.TextField(null=True, blank=True)
    propic = models.ImageField(upload_to='Profilepic')

    def __str__(self):
        return self.fullname

    def delete(self, *args, **kwargs):
        # Call parent delete method
        super().delete(*args, **kwargs)

        # Delete file when instance is deleted
        if self.propic != "Profilepic/defaultavater.png":
            if os.path.isfile(self.propic.path):
                os.remove(self.propic.path)
        else:
            return HttpResponse("Default Profile Picture Cannot be Deleted!")