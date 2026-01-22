from django.db import models

# Create your models here.

class Education(models.Model):
    degree_title = models.CharField(max_length=200)
    institution = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField()

    def __str__(self):
        return f"{self.degree_title} - {self.institution}"

    class Meta:
        verbose_name = "Education"
        verbose_name_plural = "Education"