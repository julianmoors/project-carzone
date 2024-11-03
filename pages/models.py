from django.db import models

class Member(models.Model):
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    job_title = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    facebook_link = models.URLField(max_length=100)
    twitter_link = models.URLField(max_length=100)
    g_plus_link = models.URLField(max_length=100)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name
