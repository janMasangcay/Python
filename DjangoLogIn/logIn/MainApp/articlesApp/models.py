from django.db import models

# Create your models here.
class Article(models.Model): # This is inheriting what the model from Django has
    title = models.CharField(max_length=100) # Setting this field to 100 characters only
    slug = models.SlugField() # a short label for something, containing only letters, numbers, underscores or hyphens. They’re generally used in URLs.
    body = models.TextField() # a large TextField
    date = models.DateTimeField(auto_now_add=True) # Automatically set the field to now when the object is first created.
    # add in thumbnail later
    # add in author later
