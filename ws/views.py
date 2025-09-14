from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView

class RegionListView(APIView):
    def get(self, request):
        data = [  
            {
                "identifier": "altmash ki gand",
                "latitude": 27.733333,
                "longitude": 88.55,
                "radius": 50000,
                "notifyOnEnter": True,
                "notifyOnExit": True,
                "entered": False
            },
            {
                "identifier": "Lachen",
                "latitude": 27.733333,
                "longitude": 88.55,
                "radius": 5000,
                "notifyOnEnter": True,
                "notifyOnExit": True,
                "entered": False
            },
            {
                "identifier": "Yumthang Valley, Yumthang",
                "latitude": 27.825926,
                "longitude": 88.695831,
                "radius": 5000,
                "notifyOnEnter": True,
                "notifyOnExit": True,
                "entered": False
            },
            {
                "identifier": "Chungthang",
                "latitude": 27.605,
                "longitude": 88.609,
                "radius": 5000,
                "notifyOnEnter": True,
                "notifyOnExit": True,
                "entered": False
            },
            {
                "identifier": "Noney (NH-37) Noney",
                "latitude": 24.859,
                "longitude": 93.633,
                "radius": 5000,
                "notifyOnEnter": True,
                "notifyOnExit": True,
                "entered": False
            },
            {
                "identifier": "Barak Valley",
                "latitude": 24.833,
                "longitude": 92.7789,
                "radius": 5000,
                "notifyOnEnter": True,
                "notifyOnExit": True,
                "entered": False
            },
            {
                "identifier": "Kohima (NH-2)",
                "latitude": 25.634,
                "longitude": 94.098,
                "radius": 5000,
                "notifyOnEnter": True,
                "notifyOnExit": True,
                "entered": False
            },
            {
                "identifier": "Shillong",
                "latitude": 25.2,
                "longitude": 92.033333,
                "radius": 5000,
                "notifyOnEnter": True,
                "notifyOnExit": True,
                "entered": False
            },
            {
                "identifier": "Itanagar Hills",
                "latitude": 27.1,
                "longitude": 93.616667,
                "radius": 5000,
                "notifyOnEnter": True,
                "notifyOnExit": True,
                "entered": False
            }
        ]
        return Response(data)
