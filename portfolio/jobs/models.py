from django.db import models

class Job(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length =250)
    summary = models.CharField(max_length = 500)
    ios_url = models.URLField(max_length = 200,blank=True)
    droid_url =  models.URLField(max_length = 200,blank=True)
    job_url = models.URLField(max_length = 200,blank=True)
    video_url = models.URLField(max_length = 400,blank=True)
    download_url = models.URLField(max_length=200, blank=True)

    def __str__(self):
        return self.title
