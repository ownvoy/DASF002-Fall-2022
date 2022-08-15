from django.shortcuts import render
from rest_framework.views import APIView
import json
from google import Chrome
from search.models import Data

class Sub(APIView):
    def get(self, request):
        print("get으로 호출")
        return render(request, "DASF002/main.html")
    def post(self, request):
        print("post로 호출")
        if request.method == 'POST':
            print("post로 넘어갔나")
            print(request.data)
            search_result = request.data.get('text', None)
            # 왜 content가 아니고 QuearyDict가 {'text': ['검색한 값']}이지
            print(search_result)
            search_list = Chrome.googleCrawling(search_result)
            # 여기 왜 self 안들어가지

            Data.objects.all().delete()
            for title, link, description in search_list:
                Data(title=title, link=link, description=description).save()
            search_list = Data.objects.all()
            return render(request, "search/search.html", context=dict(search=search_list))
        return render(request, "DASF002/main.html")
