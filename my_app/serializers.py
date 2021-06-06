from .models import *
from rest_framework import serializers

class PredictionSerialzier(serializers.ModelSerializer):

    class Meta:
        model = Predictions

        fields = '__all__'