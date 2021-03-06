from django.db import models
    
class Bookmark(models.Model):
    def __unicode__(self):
        return self.id
    id = models.CharField(primary_key=True, max_length=32)
    content = models.TextField()
    class Meta:
        ordering = ['id']
