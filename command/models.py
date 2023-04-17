from django.db import models

class Command(models.Model):
    DIFFICULTY_CHOICES = [
    ('★☆☆', '★☆☆'),
    ('★★☆', '★★☆'),
    ('★★★', '★★★'),
    ('N/A', 'N/A'),
]
    title = models.CharField(max_length=300, blank=True, null=True)
    html = models.TextField(max_length=3000, blank=True, null=True)
    css = models.TextField(max_length=3000, blank=True, null=True)
    js = models.TextField(max_length=3000, blank=True, null=True)
    difficulty = models.CharField(
        max_length=20,
        choices=DIFFICULTY_CHOICES,
        default="Not Rated",
    )
    date = models.DateField(auto_now=True, auto_now_add=False)

    class Meta:
        verbose_name_plural='Commands'

    def __str__(self):
        return self.title


