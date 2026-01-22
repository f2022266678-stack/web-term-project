from django.db import models

# Create your models here.

class Bio(models.Model):
    name = models.CharField(max_length=100)
    job_title = models.CharField(max_length=100)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    professional_description = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Bio"
        verbose_name_plural = "Bios"