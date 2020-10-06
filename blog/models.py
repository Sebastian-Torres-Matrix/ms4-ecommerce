from django.db import models


class blog(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(max_length=500)
    image = models.ImageField(upload_to="images", blank=True, null=True)

    def __unicode__(self):
        return self.title
