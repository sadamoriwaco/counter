from django.db import models

class Counter(models.Model):
    name = models.CharField(max_length=100)
    count1 = models.IntegerField(default=0)
    count2 = models.IntegerField(default=0)
    count3 = models.IntegerField(default=0)
    count4 = models.IntegerField(default=0)

    def __str__(self):
        return self.name
