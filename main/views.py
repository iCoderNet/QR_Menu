from django.shortcuts import render
from django.views import View

class MainView(View):
    def get(self, request):
        return render(request, 'index.html')
    
class PageHTMLView(View):
    def get(self, request, page):
        return render(request, page)