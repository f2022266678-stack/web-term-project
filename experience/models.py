from django.db import models

# Create your models here.

class Experience(models.Model):
    role = models.CharField(max_length=200)
    company_or_institution = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    is_current = models.BooleanField(default=False)
    description = models.TextField()

    def __str__(self):
        return f"{self.role} at {self.company_or_institution}"

    class Meta:
        verbose_name = "Experience"
        verbose_name_plural = "Experiences"