from rest_framework import serializers
from .models import Confirmed, Death, Recovery

class ConfirmedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Confirmed
        fields = ('country', 'startdate', 'enddate', 'counts')

class DeathSerializer(serializers.ModelSerializer):
    class Meta:
        model = Death
        fields = ('country', 'startdate', 'enddate', 'counts')

class RecoverySerializer(serializers.ModelSerializer):
    class Meta:
        model = Recovery
        fields = ('country', 'startdate', 'enddate', 'counts')
