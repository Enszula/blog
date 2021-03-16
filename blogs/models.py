from django.db import models

class Post(models.Model):
    """A post the user wrote"""
    title = models.CharField(max_length=50)
    text = models.CharField(max_length=2200)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'posts'

    def __str__(self):
        """Return a string representation of the model"""
        return self.title + "     " + f"{self.text[:50]}..."