from django.db import models

# Create your models here.
class Article(models.Model): # This is inheriting what the model from Django has
    title = models.CharField(max_length=100) # Setting this field to 100 characters only
    slug = models.SlugField() # a short label for something, containing only letters, numbers, underscores or hyphens. They’re generally used in URLs.
    body = models.TextField() # a large TextField
    date = models.DateTimeField(auto_now_add=True) # Automatically set the field to now when the object is first created.
    # add in thumbnail later
    # add in author later

    def __str__(self):    # Shows a more meaningful result when querying data from the DB instead of just "objName object (2), objName object (1)"
        return self.title

    def snippet(self):    # Added this function to manipulate the display and shorten for the articleList page.
        return self.body[:50] + '...'



# After creating model, let Django knows that you want to show this update to the admin-area view. -Inside articles.admin.py 

"""
Interacting with data into the Database(ENV is ON) using python shell:
-manage.py shell
>>> from appName.models import classInsideTheModel # classInsideTheModel also the name of the table inside the DB
>>> classInsideTheModel # this is to confirm we targetted the model
>>> classInsideTheModel.objects.all() # query available object inside the database
>>> objName = classInsideTheModel() # create new instance of that class 
>>> objName.title = "Putok, this is the title" # .title is a property of that classa and assigning a value to that property
>>> objName.title # returns the value inside that property
>>> objName.save() # saves this object instance to the DB
>>> classInsideTheModel.objects.all() # query available object inside the database
>>> classInsideTheModel.objects.all()[0] # query specific object into the DB
"""