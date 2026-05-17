from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, "Draft"), (1, "Published"))

# Create your models here.
class Score(models.Model):
    score_name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique=True)
    composer = models.ManyToManyField('Composer', related_name='scores')
    youtube_url = models.URLField()
    score_description = models.TextField()
    release_date = models.DateField()
    score_created_at = models.DateTimeField(auto_now_add=True)
    score_updated_at = models.DateTimeField(auto_now=True)
    score_deleted = models.BooleanField("deleted", default=False)
    status = models.IntegerField(choices=STATUS, default=0)
    
    class Meta: 
        ordering = ["-score_created_at"]
    
    # Code from Microsoft Copilot 
    def __str__(self):
        composers = ", ".join(c.composer_name for c in self.composer.all())
        return f"{self.score_name} | composed by {composers}"


class Composer(models.Model):
    composer_name = models.CharField(max_length=255)
    composer_birth_date = models.DateField()
    composer_death_date = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return self.composer_name

class Track(models.Model):
    score = models.ForeignKey('Score', on_delete=models.CASCADE, related_name='tracks')
    track_name = models.CharField(max_length=250)
    track_length = models.DurationField()
