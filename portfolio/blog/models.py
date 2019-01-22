from django.db import models
import datetime

class Blog(models.Model):
    title       =   models.CharField(max_length = 50)
    pub_date    =   models.DateTimeField(null = True)
    body        =   models.TextField(max_length = 340)
    image       =   models.ImageField(upload_to='images/')

    def summary(self):
        return self.body[:100] +"..."

    def pub_date_pr(self):
        return self.pub_date.strftime('%e %b %Y')

    def __str__(self):
        return self.title
