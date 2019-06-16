from django.shortcuts import render
from .models import Article 

# Create your views here.
def articleList(request):
    articlesPutok = Article.objects.all().order_by('date')
    return render(request, 'articles/articleList.html', {'articlesAnglit': articlesPutok}) # articles/ is from the template inside articlesApp


# from .models import Article - to access the information inside tye DB (import . to import all class/object)
# line 6 is getting ALL data inside the Articles table from the DB
# , {'articlesAnglit': articlesPutok} - includes on rendering info to the front-end

"""{% articlesAnglit %} - this is to use python code called template tag (equivalent of razer syntax in C#)
{{ }} output information out of python code"""