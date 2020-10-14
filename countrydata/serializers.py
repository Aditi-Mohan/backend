from rest_framework import serializers
from .models import Data, Subscriber, Sentdate

class DataSerializer(serializers.ModelSerializer):
    country = serializers.CharField()
    confirmed = serializers.ListField(child=serializers.IntegerField())
    startdate = serializers.CharField()
    enddate = serializers.CharField()
    currconfirmed = serializers.IntegerField()
    death = serializers.ListField(child=serializers.IntegerField())
    currdeath = serializers.IntegerField()
    recovery = serializers.ListField(child=serializers.IntegerField())
    currrecovery = serializers.IntegerField()
    active = serializers.ListField(child=serializers.IntegerField())
    curractive = serializers.IntegerField()
    rank = serializers.IntegerField()
    
    class Meta:
        model = Data
        fields = (
            'country', 'confirmed', 'startdate', 'enddate', 'currconfirmed',
            'death', 'currdeath', 'recovery', 'currrecovery', 'active', 'curractive', 'rank'
            )

class SubscriberSerializer(serializers.ModelSerializer):
    uid = serializers.IntegerField()
    email = serializers.CharField()
    watchlist = serializers.CharField()
    top5 = serializers.BooleanField()

    class Meta:
        model = Subscriber
        fields = (
            'uid', 'email', 'watchlist', 'top5'
        )

class SentdateSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    date = serializers.CharField()

    class Meta:
        model = Sentdate
        fields = ('id', 'date')