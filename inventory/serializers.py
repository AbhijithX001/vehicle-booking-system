from rest_framework import serializers
from .models import Vehicle, Booking
from datetime import date

class VehicleSerializer(serializers.ModelSerializer):

    class Meta:
        model =Vehicle
        fields='__all__'
    
class BookingSerializer(serializers.ModelSerializer):
    vehicle_details=VehicleSerializer(source='vehicle', read_only=True)

    class Meta:
        model = Booking
        fields = ['id', 'vehicle', 'vehicle_details', 'customer_name', 
                  'customer_phone', 'start_date', 'end_date', 'total_amount', 'created_at']
        read_only_fields = ['total_amount', 'created_at']

    def validate_customer_phone(self,value):
        if len(value)!=10:
            raise serializers.ValidationError("phone numbers must be exactly 10 digits")
        if not value.isdigit():
            raise serializers.ValidationError("phone number should only contain digits")
        
        return value
    
    def validate(self, data):
        if data['start_date']< date.today():
            raise serializers.ValidationError("start date is in the past, it cannot be like that")
        if data['end_date']<= data['start_date']:
            raise serializers.ValidationError("end date is before start date, it cant be like that")
        
        vehicle = data['vehicle']

        overlapping = Booking.objects.filter(
            vehicle=vehicle,
            start_date__lte=data['end_date'],  
            end_date__gte=data['start_date']   
            )
        if self.instance:
            overlapping=overlapping.exclude(pk=self.instance.pk)
        if overlapping.exists():
            raise serializers.ValidationError("the vehicle is already booked, please try a diff one")
        return data
    
    def create(self,validated_data):
        days= (validated_data['end_date']-validated_data['start_date']).days
        vehicle= validated_data['vehicle']
        validated_data['total_amount']= days*vehicle.price_per_day

        booking= Booking.objects.create(**validated_data)
        vehicle.is_available= False
        vehicle.save()
        return booking
    

    


