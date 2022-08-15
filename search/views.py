from django.shortcuts import render

from google import Chrome
from .models import Data
from rest_framework.views import APIView




class Main(APIView):
    def get(self, request):
        search_list = Chrome.googleCrawling(search_term="자바")
        # 여기 왜 self 안들어가지
        for title, link, description in search_list:
            Data(title=title, link=link, description=description).save()
        search_list = Data.objects.all()

        return render(request, "search/search.html", context=dict(search=search_list))


# Create your views here.
