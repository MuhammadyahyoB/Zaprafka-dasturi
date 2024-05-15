from django.shortcuts import render
from rest_framework import generics
from . import serializers
from main import models

# ------------ Create  UPDATE, DELETE, LIST, DETAIL -------

# LIST
class CategoryApiViewlist(generics.ListAPIView):
    """ cATEGORY viewlist """
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer

# Create
class CategoryApiViewCreate(generics.CreateAPIView):
    """ CATEGORY view create """
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer


# Detail
class CategoryApiViewDetail(generics.RetrieveUpdateDestroyAPIView):
    """ CATEGORY view detail """
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer


# -------------- Yoqilgituri  CREATE, DETAIL, LIST, UPDATE -------------

# LIST
class YoqilgituriApiViewlist(generics.ListAPIView):
    """ Yoqilgituri view list """
    queryset = models.Yoqilgituri.objects.all()
    serializer_class = serializers.YoqilgituriSerializer

# Create
class YoqilgituriAppViewCreate(generics.CreateAPIView):
    """ Yoqilgituri view create """
    queryset = models.Yoqilgituri.objects.all()
    serializer_class = serializers.YoqilgituriSerializer


# Detail
class YoqilgituriAppViewDetail(generics.RetrieveUpdateDestroyAPIView):
    """ Yoqilgituri view detail """
    queryset = models.Yoqilgituri.objects.all()
    serializer_class = serializers.YoqilgituriSerializer



# -------------- Zaprafka  CREATE, DETAIL, LIST, UPDATE -------------
    

# LIST
class ZaprafkaAppViewList(generics.ListAPIView):
    """ Zaprafka view list """
    queryset = models.Zaprafka.objects.all()
    serializer_class = serializers.ZaprafkaSerializer

# Create
class ZaprafkaAppViewCreate(generics.CreateAPIView):
    """ Zaprafka view create """
    queryset = models.Zaprafka.objects.all()
    serializer_class = serializers.ZaprafkaSerializer


# Detail
class ZaprafkaAppViewDetail(generics.RetrieveUpdateDestroyAPIView):
    """ Zaprafka view detail """
    queryset = models.Zaprafka.objects.all()
    serializer_class = serializers.ZaprafkaSerializer

    


