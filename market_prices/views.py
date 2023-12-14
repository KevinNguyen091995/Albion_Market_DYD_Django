from rest_framework.response import Response
from rest_framework import status, generics
from django.db.models import Q
from .models import MarketPricesModel
from .serializers import MarketPricesSerializer
from datetime import datetime, timedelta
from django.db.models import Max

class MarketPricesDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MarketPricesModel.objects.all()
    serializer_class = MarketPricesSerializer
    lookup_field = 'ItemTypeId'

class MarketPricesView(generics.ListAPIView):
    queryset = MarketPricesModel.objects.all()
    serializer_class = MarketPricesSerializer

    def post(self, request, *args, **kwargs):
        # Try to get an existing record based on ItemTypeId and QualityLevel
        item_type_id = request.data.get('ItemTypeId')
        quality_level = request.data.get('QualityLevel')
        existing_instance = MarketPricesModel.objects.filter(Q(ItemTypeId=item_type_id) & Q(QualityLevel=quality_level)).first()

        if existing_instance:
            # If the record already exists, update it
            serializer = MarketPricesSerializer(instance=existing_instance, data=request.data)

            if serializer.is_valid():
                # Extract data from the serializer
                new_unit_price = serializer.validated_data.get('UnitPriceSilver')
                new_timestamp = serializer.validated_data.get('last_updated')

                # Check if new_timestamp is not None and is over 1 hour older than the current time
                current_time = datetime.now()
                if new_timestamp and (new_timestamp <= current_time and new_timestamp >= current_time - timedelta(hours=1)):
                    # Check if the new_unit_price is less than what is currently in the database
                    current_max_unit_price = MarketPricesModel.objects.filter(Q(ItemTypeId=item_type_id) & Q(QualityLevel=quality_level)).aggregate(Max('UnitPriceSilver'))['UnitPriceSilver__max']
                    if current_max_unit_price is not None and new_unit_price < current_max_unit_price:
                        # Update the existing model
                        serializer.save()
                        return Response(serializer.data, status=status.HTTP_200_OK)

                    else:
                        return Response(status=status.HTTP_400_BAD_REQUEST)

                else:
                    return Response(status=status.HTTP_400_BAD_REQUEST)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        else:
            # If the record doesn't exist, create a new one
            serializer = self.get_serializer(data=request.data)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)