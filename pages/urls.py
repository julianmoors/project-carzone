from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('', views.home_view, name='home'),
    path('about', views.about_view, name='about'),
    path('services', views.services_view, name='services'),
    path('contact', views.contact_view, name='contact'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
