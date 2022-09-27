from django.db import connection
from django.db.models import Count
from django.shortcuts import render
from rest_framework.views import APIView
from serpapi import GoogleSearch

from categorize import Categorizer
# from google import Chrome
from search.models import Academic, Data, News, Org, Research


class Sub(APIView):
    def get(self, request):
        print("get으로 호출")
        return render(request, "DASF002/main.html")

    def post(self, request):
        print("post로 호출")
        if request.method == "POST":
            print("post로 넘어갔나")
            print(request.data)
            search_result = request.data.get("text", None)
            print(search_result)

            params = {
                "q": search_result,
                "hl": "ko",
                "gl": "kr",
                "start": 0,
                "num": 100,
                "api_key": "de9fb63c0984552b04736c6ec26dfc408a9d4ed6f3e4d4e5b9d63d1f42c69af0",
            }

            search = GoogleSearch(params)
            results = search.get_dict()

            Data.objects.all().delete()
            Academic.objects.all().delete()
            Research.objects.all().delete()
            Org.objects.all().delete()
            News.objects.all().delete()
            categorizer = Categorizer()
            for element in results["organic_results"]:
                if "snippet" not in element:
                    element["snippet"] = "There is No description"
                category = categorizer.get_category(element["link"])
                if category == "other":
                    continue
                Data(
                    title=element["title"],
                    link=element["link"],
                    description=element["snippet"],
                    category=category,
                ).save()
                categorizer.save(category, element)
            news = News.objects.all()
            academic = Academic.objects.all()
            org = Org.objects.all()
            research = Research.objects.all()
            return render(
                request,
                "search/search.html",
                context=dict(
                    news=news,
                    academic=academic,
                    org=org,
                    research=research,
                ),
            )
        return render(request, "DASF002/main.html")
