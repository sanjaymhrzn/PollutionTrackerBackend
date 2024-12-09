from django.urls import path
from .views import PollutionDataView

urlpatterns = [
    path('combined_data/', PollutionDataView.as_view(), name='combined_data'),
]