from django.db import models


class Brewery(models.Model):
    name = models.CharField(max_length=300)
    country = models.CharField(max_length=60, default="Polska")
    location = models.CharField(max_length=100)
    year = models.IntegerField(blank=True, default=0)


    def __str__(self):
        return self.name


class Malt(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Style(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField()

    def __str__(self):
        return self.name
    

class Beer(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField()
    style = models.ForeignKey(Style, on_delete=models.CASCADE)
    brewery = models.ForeignKey(Brewery, on_delete=models.CASCADE)
    blg = models.FloatField(blank=True)
    ibu = models.IntegerField(blank=True)
    malt = models.BinaryField(models.ForeignKey(Malt, on_delete=models.CASCADE))

    def __str__(self):
        return self.name
    

