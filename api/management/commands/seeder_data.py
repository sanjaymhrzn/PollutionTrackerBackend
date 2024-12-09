from django.core.management.base import BaseCommand
import random
from datetime import date, timedelta
from api.models import PollutionData

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        PollutionData.objects.all().delete()
        date_value=date(2015, 1, 1)
        for i in range(500):
            random_value=random.randint(4, 10)
            date_value = date_value +timedelta(days=random_value)
            pollution_data = PollutionData(
                date=date_value,
                air_quality_index=random.randint(50, 200),
                water_quality_index=random.randint(70, 100),
                ph_level=round(random.uniform(6.5, 8.5), 1),
                temperature=round(random.uniform(20.0, 35.0), 1),
            )
            pollution_data.save()
        print("completed")