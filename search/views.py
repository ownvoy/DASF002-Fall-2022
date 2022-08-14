from django.shortcuts import render
from .models import Data
from rest_framework.views import APIView

class Main(APIView):
    def get(self, request):
        search_list = Data.objects.all()

        return render(request, "search/search.html", context=dict(search=search_list))


# Create your views here.
