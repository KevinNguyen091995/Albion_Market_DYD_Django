from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListAPIView
from .models import MarketPricesModel
from .serializers import MarketPricesSerializer
from datetime import datetime, timedelta
from django.db.models import Max

class MarketPricesView(ListAPIView):
    queryset = MarketPricesModel.objects.all()
    serializer_class = MarketPricesSerializer

    def post(self, request, *args, **kwargs):
        serializer = MarketPricesSerializer(data=request.data)

        if serializer.is_valid():
            # Extract data from the serializer
            new_unit_price = serializer.validated_data.get('UnitPriceSilver')
            new_timestamp = serializer.validated_data.get('last_updated')

            # Check if new_timestamp is not None and is over 1 hour older than the current time
            current_time = datetime.now()
            if new_timestamp and (new_timestamp >= current_time or new_timestamp <= current_time - timedelta(hours=1)):
                # Check if the new_unit_price is less than what is currently in the database
                current_max_unit_price = MarketPricesModel.objects.aggregate(Max('UnitPriceSilver'))['UnitPriceSilver__max']
                if current_max_unit_price is not None and new_unit_price < current_max_unit_price:
                    # Update the model
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                else:
                    return Response({"error": "New unit price must be less than the current maximum unit price."},
                                    status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({"error": "New timestamp must be over 1 hour older than the current time."},
                                status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)