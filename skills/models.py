from django.db import models

# Create your models here.

class Skill(models.Model):
    CATEGORY_CHOICES = [
        ('Technical', 'Technical'),
        ('Professional', 'Professional'),
    ]
    
    name = models.CharField(max_length=100)
    proficiency = models.IntegerField(help_text="Proficiency level as percentage (0-100)")
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)

    def __str__(self):
        return f"{self.name} ({self.category})"

    class Meta:
        verbose_name = "Skill"
        verbose_name_plural = "Skills"