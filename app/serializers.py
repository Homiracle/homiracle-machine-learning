from rest_framework import serializers
from app.models import Reservation

class ReservationSerializers(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'
