from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, "Draft"), (1, "Published"))

# Create your models here.
class Score(models.Model):
    score_name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique=True)
    composer = models.ManyToManyField('Composer', related_name=scores)
    youtube_url = models.URLField()
    score_description = models.TextField()
    score_runtime = models.DurationField()
    release_date = models.DateField()
    score_created_at = models.DateTimeField(auto_now_add=True)
    score_updated_at = models.DateTimeField(auto_now=True)
    score_deleted = models.BooleanField("deleted", default=False)
    status = models.IntegerField(choices=STATUS, default=0)
    
def __str__(self):
    return self.score_name

    
    
class Composer(models.Model):
    composer_name = models.CharField(max_length=255)
    composer_birth_date = models.DateField()
    composer_death_date = models.DateField(null=True, blank=False)
    

    def __str__(self):
        return self.composer_name
