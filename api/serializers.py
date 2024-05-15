from main import models

from rest_framework import serializers


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = '__all__'


class YoqilgituriSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Zaprafka
        fields = '__all__'


class ZaprafkaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Zaprafka 
        fields = '__all__'


class Zaprafkacategoryserializer(serializers.ModelSerializer):
    class Meta:
        model = models.Zaprafkacategory
        fields = '__all__'


