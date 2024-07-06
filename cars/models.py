from django.db import models
from datetime import datetime
from django_ckeditor_5.fields import CKEditor5Field


class Car(models.Model):
    state_choices = (
        ('AL', 'Alabama'),
        ('AK', 'Alaska'),
        ('AZ', 'Arizona'),
        ('AR', 'Arkansas'),
        ('CA', 'California'),
        ('CO', 'Colorado'),
        ('CT', 'Connecticut'),
        ('DE', 'Delaware'),
        ('DC', 'District of Columbia'),
        ('FL', 'Florida'),
        ('GA', 'Georgia'),
        ('HI', 'Hawaii'),
        ('ID', 'Idaho'),
        ('IL', 'Illinois'),
        ('IN', 'Indiana'),
        ('IA', 'Iowa'),
        ('KS', 'Kansas'),
        ('KY', 'Kentucky'),
        ('LA', 'Louisiana'),
        ('ME', 'Maine'),
        ('MD', 'Maryland'),
        ('MA', 'Massachusetts'),
        ('MI', 'Michigan'),
        ('MN', 'Minnesota'),
        ('MS', 'Mississippi'),
        ('MO', 'Missouri'),
        ('MT', 'Montana'),
        ('NE', 'Nebraska'),
        ('NV', 'Nevada'),
        ('NH', 'New Hampshire'),
        ('NJ', 'New Jersey'),
        ('NM', 'New Mexico'),
        ('NY', 'New York'),
        ('NC', 'North Carolina'),
        ('ND', 'North Dakota'),
        ('OH', 'Ohio'),
        ('OK', 'Oklahoma'),
        ('OR', 'Oregon'),
        ('PA', 'Pennsylvania'),
        ('RI', 'Rhode Island'),
        ('SC', 'South Carolina'),
        ('SD', 'South Dakota'),
        ('TN', 'Tennessee'),
        ('TX', 'Texas'),
        ('UT', 'Utah'),
        ('VT', 'Vermont'),
        ('VA', 'Virginia'),
        ('WA', 'Washington'),
        ('WV', 'West Virginia'),
        ('WI', 'Wisconsin'),
        ('WY', 'Wyoming'),
    )

    year_choices = []
    for num in range(2000, (datetime.now().year + 1)):
        year_choices.append((num, num))

    condition_choices = (
        ('NEW', 'New'),
        ('USED', 'Used'),
    )

    door_choices = (
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
    )

    title = models.CharField(max_length=255)
    state = models.CharField(choices=state_choices, max_length=100)
    city = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField(('year'), choices=year_choices)
    condition = models.CharField(choices=condition_choices, max_length=4)
    price = models.IntegerField()
    description = CKEditor5Field('Text', config_name='extends')
    car_photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    car_photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    car_photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    car_photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    car_photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    cruise_control = models.BooleanField(default=False)
    audio_interface = models.BooleanField(default=False)
    airbags = models.BooleanField(default=False)
    air_conditioning = models.BooleanField(default=False)
    seat_heating = models.BooleanField(default=False)
    alarm_system = models.BooleanField(default=False)
    park_assist = models.BooleanField(default=False)
    power_steering = models.BooleanField(default=False)
    reversing_camera = models.BooleanField(default=False)
    direct_fuel_injection = models.BooleanField(default=False)
    auto_start = models.BooleanField(default=False)
    wind_deflector = models.BooleanField(default=False)
    bluetooth_handset = models.BooleanField(default=False)
    body_type = models.CharField(max_length=100)
    engine = models.CharField(max_length=100)
    transmission = models.CharField(max_length=100)
    interior = models.CharField(max_length=100)
    mileage = models.IntegerField()
    doors = models.CharField(choices=door_choices, max_length=1)
    passengers = models.IntegerField()
    vin_no = models.CharField(max_length=100)
    fuel_type = models.CharField(max_length=100)
    no_owners = models.IntegerField()
    is_featured = models.BooleanField(default=False)
    created_date = models.DateField(default=datetime.now, blank=True)

    def __str__(self):
        return self.title
