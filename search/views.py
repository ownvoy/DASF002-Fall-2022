from django.shortcuts import render
from rest_framework.views import APIView

from .models import Data


class Main(APIView):
    def get(self, request):
        return render(request, "search/search.html", context=dict(search=search_result_groupby))


# Create your views here.
