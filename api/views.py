from rest_framework.generics import GenericAPIView
from .models import PollutionData
from .serializers import PollutionDataSerializer
from rest_framework.response import Response
from.utils import get_mock_data,get_weather_data
import time
class PollutionDataView(GenericAPIView):
    serializer_class = PollutionDataSerializer

    def post(self, request, *args, **kwargs):
        try:
            start_data=self.request.data["start_date"]
            end_date=self.request.data["end_date"]
            sensor_data=get_mock_data()
            historical_data = PollutionData.objects.filter(date__gte=start_data, date__lte=end_date)
            historical_serializer = self.get_serializer(historical_data, many=True)
            weather_data=get_weather_data()
            combined_data = {
                "live_sensor_data": sensor_data,
                "historical_data": historical_serializer.data,
                "weather_data": weather_data,
            }
            time.sleep(4)
            return Response(combined_data, status=200)
        except Exception as e:
            print("error",e)
            return Response({"message":"Some error occurred" }, status=500)
