from django.shortcuts import render

# Create your views here.
def articleList(request):
    return render(request, 'articles/articleList.html') # articles/ is from the template inside articlesApp