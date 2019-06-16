from django.contrib import admin
from .models import Article
# Register your models here.

admin.site.register(Article)

# add - from .models import Article (. in .models is the saying the current dir)
# admin.site.register(Article) - telling Django to register Article class(OBJECT) from models.py