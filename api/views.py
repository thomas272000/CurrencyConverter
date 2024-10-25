import requests
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import ConversionModel
from .serializers import ConversionSerializer


# Create your views here.

API_URL = 'https://v6.exchangerate-api.com/v6/d84978a6f65de1281f2b766c/latest/'

class ConvertCurrencyAPIView(APIView):
    def post(self, request):
        from_currency = request.data.get('from_currency')
        to_currency = request.data.get('to_currency')
        amount = float(request.data.get('amount', 1))

        # To Fetch conversion rate from API
        response = requests.get(f'{API_URL}/{from_currency}')
        
        if response.status_code != 200:
            return Response(
                {"error": f"API request failed with status code {response.status_code}. Message: {response.text}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

        try:
            data = response.json()
        except ValueError:
            return Response(
                {"error": "Failed to parse response from the currency API."},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

        if 'conversion_rates' in data and to_currency in data['conversion_rates']:
            rate = data['conversion_rates'][to_currency]
            converted_amount = round(amount * rate, 2)

            # To Save the conversion record
            conversion = ConversionModel.objects.create(
                from_currency=from_currency,
                to_currency=to_currency,
                amount=amount,
                converted_amount=converted_amount,
                rate=rate
            )
            serializer = ConversionSerializer(conversion)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({"error": "Invalid currency code or API issue."}, status=status.HTTP_400_BAD_REQUEST)

# To fetch History
class ConversionHistoryAPIView(APIView):
    def get(self, request):
        conversions = ConversionModel.objects.all().order_by('-date')[:5]
        serializer = ConversionSerializer(conversions, many=True)
        return Response(serializer.data)