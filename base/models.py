from django.db import models


class ContactFormResponse(models.Model):
    name = models.CharField(max_length=100)  # string - required
    email = models.CharField(max_length=100)  # string - required
    subject = models.CharField(max_length=100)  # string - required
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return str(self.name)
