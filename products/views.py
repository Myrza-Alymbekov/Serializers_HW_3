import json

from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets, generics

from .models import Item, Brand, Category
from.serializers import ItemSerializer, BrandSerializer


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class BrandCreateListView(generics.ListCreateAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


class BrandRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


@csrf_exempt
def create_category(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        new_category = Category.objects.create(**data)
        json_data = {
            "name": new_category.name
        }
        return JsonResponse(json_data, safe=False)
    if request.method == 'GET':
        categories = Category.objects.all()
        data = []
        for category in categories:
            data.append(
                {
                    'name': category.name
                }
            )
        json_data = json.dumps(data)
        return JsonResponse(json_data, safe=False)


