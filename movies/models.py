from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=200)
    year = models.IntegerField()

    #overide to change how string object is rendered on the admin page
    def __str__(self):
        return f'{self.title} from {self.year}'