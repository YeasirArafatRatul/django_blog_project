from django.shortcuts import render
import datetime
from rest_framework import generics
from django.utils import timezone
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import KeyValue
from .serializers import KeyValueSerializer
from .tasks import time_to_live

# Create your views here.
class KeyValueRUDApiView(generics.RetrieveUpdateDestroyAPIView):
    lookup_url_kwarg = 'key'
    serializer_class = KeyValueSerializer
    queryset = KeyValue.objects.all()

    def put(self, request, key):
        key = self.kwargs.get("key")
        instance = KeyValue.objects.get(key=key)
        TTL = datetime.timedelta(minutes=5)
        new_time = timezone.now()+TTL
        instance.timestamp = new_time
        instance.save()
        time_to_live(key)
        return super().put(request)

    def patch(self, request, key):
        key = self.kwargs.get("key")
        instance = KeyValue.objects.get(key=key)
        TTL = datetime.timedelta(minutes=5)
        new_time = timezone.now()+TTL
        instance.timestamp = new_time
        instance.save()
        time_to_live(key)
        return super().patch(request)


class allPairsAPI(generics.ListAPIView):
    serializer_class = KeyValueSerializer
    queryset = KeyValue.objects.all()


class addPairView(generics.CreateAPIView):
    lookup_url_kwarg = 'key'
    serializer_class = KeyValueSerializer

    def create(self, request):
        data = request.data
        serializer = KeyValueSerializer(data=data)
        key = data['key']
        if serializer.is_valid():
            serializer.save()
            time_to_live(key)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)