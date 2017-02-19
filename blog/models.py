from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=255)
    #description = models.CharField(max_length=255, null=True, default='')

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=200)
   # slug = models.SlugField(max_length=100, unique=True)
    body = models.TextField()
    posted = models.DateTimeField()
    tags = models.ManyToManyField(Tag)

    def __unicode__(self):
        return '%s' % self.title

    class Meta:
        ordering = ['posted']




 #   def __unicode__(self):
 #       return '%s' % self.title

