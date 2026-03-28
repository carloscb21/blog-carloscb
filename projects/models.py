from django.db import models
from django.utils.text import slugify
from blog.models import Tag

class Project(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    description = models.TextField()
    url = models.URLField(blank=True)
    repo_url = models.URLField(blank=True)
    tags = models.ManyToManyField(Tag, blank=True, related_name='projects')
    order = models.IntegerField(default=0)
    active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
