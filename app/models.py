from django.db import models

class Reservation(models.Model):
    user_id = models.IntegerField()
    room_id = models.IntegerField()
    end_date = models.DateField()

class Weather(models.Model):
    '''This model save all fields of the daily weather'''
    date = models.DateField()
    temperatureMax = models.FloatField()
    windBearing = models.FloatField()
    dewPoint = models.FloatField()
    cloudCover= models.FloatField()
    windSpeed= models.FloatField()
    pressure= models.FloatField()
    apparentTemperatureHigh= models.FloatField()
    visibility= models.FloatField()
    apparentTemperatureLow= models.FloatField()
    apparentTemperatureMax= models.FloatField()
    uvIndex= models.FloatField()
    time= models.FloatField()
    temperatureLow= models.FloatField()
    temperatureMin= models.FloatField()
    temperatureHigh= models.FloatField()
    apparentTemperatureMin= models.FloatField()
    moonPhase= models.FloatField()
    clearday= models.FloatField()
    cloudy= models.FloatField()
    fog= models.FloatField()
    partly_cloudy_day= models.FloatField()
    partly_cloudy_night= models.FloatField()
    wind= models.FloatField()
    rain= models.FloatField()
    snow= models.FloatField()

class Holiday(models.Model):
    day = models.DateField()
    script = models.CharField(max_length = 120)

class Consumption(models.Model):
    consumption_id= models.CharField(max_length = 120)
    start_power= models.FloatField()
    end_power= models.FloatField()
    start_water= models.FloatField()
    end_water= models.FloatField()
    createdAt= models.DateField()
    date= models.DateField()
    is_last_day_of_month= models.BooleanField()
    is_first_day_of_month= models.BooleanField()
    month= models.FloatField()
    year= models.FloatField()
    room_id = models.CharField(max_length = 120)
    