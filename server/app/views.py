from django.db import transaction
from tensorflow.keras.models import load_model, Model, Sequential
import os
from rest_framework.exceptions import APIException
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ReservationSerializers
from datetime import datetime, timedelta
import pandas as pd
from django.conf import settings

from app.db import Database

db = Database()
cursor = db.get_cursor()


@api_view(['GET'])
def create_reservation(request):
    serializer = ReservationSerializers(data=request.data)
    if serializer.is_valid():
        user_id = request.data.get('user_id')
        room_id = request.data.get('room_id')
        end_date_str = request.data.get('end_date')

        
        end_date_transform = datetime.strptime(end_date_str, '%Y-%m-%d').date()
        end_date = end_date_transform - timedelta(days=365*11)
        start_date = end_date - timedelta(days=31)

        query = """
            SELECT *
            FROM weather
            WHERE date BETWEEN %s AND %s
        """
        with db.get_cursor() as cursor:
            cursor.execute(query, [start_date, end_date])
            weather_data = cursor.fetchall()

        query = """
            SELECT *
            FROM consumption
            WHERE roomRoomId = %s AND date BETWEEN %s AND %s
        """
        with db.get_cursor() as cursor:
            cursor.execute(query, [room_id, start_date, end_date])
            consumption_data = cursor.fetchall()
            consumption_data = pd.DataFrame(consumption_data)

        query = """
            SELECT *
            FROM holiday
        """
        with db.get_cursor() as cursor:
            cursor.execute(query)
            holiday_data = cursor.fetchall()
            holiday_data = pd.DataFrame(holiday_data)

        household = pd.DataFrame([{
            'roomRoomId': room_id,
            'ACORN': 0.0,
            'ACORN-A': 1.0,
            'ACORN-B': 1.0,
            'ACORN-C': 1.0,
            'ACORN-D': 1.0,
            'ACORN-E': 1.0,
            'ACORN-F': 1.0,
            'ACORN-G': 1.0,
            'ACORN-H': 1.0,
            'ACORN-I': 1.0,
            'ACORN-J': 1.0,
            'ACORN-K': 1.0,
            'ACORN-L': 1.0,
            'ACORN-M': 1.0,
            'ACORN-N': 1.0,
            'ACORN-O': 1.0,
            'ACORN-P': 1.0,
            'ACORN-Q': 1.0,
            'ACORN-U': 1.0,
        }])

        # merge_dataset = pd.DataFrame.merge(consumption_data, weather_data , on='day')
        # merge_dataset = pd.DataFrame.merge(merge_dataset, household, on='roomRoomId')
        # merge_dataset['isHoliday'] = merge_dataset['day'].isin(holiday_data['day']).all().astype(float)
        # merge_dataset

        file_path_data = os.path.join(settings.BASE_DIR, 'data', 'comsumption.csv')
        file_path_model = os.path.join(settings.BASE_DIR, 'ml', 'lstm_model.h5')

        data = pd.read_csv(file_path_data)
        data['day'] = pd.to_datetime(data['day']).dt.date
        filtered_data = data[(data['day'] >= start_date) & (data['day'] <= end_date)]
        filtered_data = filtered_data.drop(['day'], axis=1)
    
        model = load_model(file_path_model, compile=False)

        prediction = model.predict(filtered_data)
        return Response(prediction)
        

        
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)