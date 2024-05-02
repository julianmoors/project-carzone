from django.contrib import admin
from django.utils.html import format_html

from . models import Car

class CarAdmin(admin.ModelAdmin):
    fieldsets = (
        ('', {
            'fields': (
                'title',
                'state',
                'city',
                'color',
                'model',
                'year',
                'condition',
                'price',
                'description',
                'car_photo_1',
                'car_photo_2',
                'car_photo_3',
                'car_photo_4',
                'car_photo_5',
            ),
        }),
        ('Features', {
            'fields': (
                'cruise_control',
                'audio_interface',
                'airbags',
                'air_conditioning',
                'seat_heating',
                'alarm_system',
                'park_assist',
                'power_steering',
                'reversing_camera',
                'direct_fuel_injection',
                'auto_start',
                'wind_deflector',
                'bluetooth_handset',
            ),
        }),
        ('', {
            'fields': (
                'body_type',
                'engine',
                'transmission',
                'interior',
                'mileage',
                'doors',
                'passengers',
                'vin_no',
                'fuel_type',
                'no_owners',
                'is_featured',
                'created_date',
            ),
        }),
    )

    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" style="border-radius: 50%">'.format(object.car_photo_1.url))

    search_fields = ('title', 'model', 'city', 'state')
    thumbnail.short_description = 'Photo'

    list_display = ('thumbnail', 'title', 'model', 'year', 'city', 'state', 'mileage', 'condition', 'is_featured')
    list_editable = ('is_featured',)
    list_display_links = ('title',)
    list_filter = ('title', 'model', 'year', 'city', 'state')

admin.site.register(Car, CarAdmin)
