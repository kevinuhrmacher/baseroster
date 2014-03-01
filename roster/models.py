from django.db import models

# Create your models here.

class Player(models.Model):
    number = models.IntegerField(unique=True, null=True, max_length=2, verbose_name="No.")
    name = models.CharField(max_length=70)
    class Meta(object):
        verbose_name_plural = "Players"
        ordering = ('name', 'number')
    
    def __unicode__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        super(Player, self).save(*args, **kwargs)
        
    imgurl = models.TextField(null=True)
    dominant_hand = models.CharField(null=True, max_length=3)
    position = models.CharField(null=True, max_length=6)
    height = models.CharField(null=True, max_length=3, verbose_name="Height")
    weight = models.CharField(null=True, max_length=3, verbose_name="Weight")
    year = models.CharField(null=True, max_length=30)
    hometown = models.TextField(null=True, verbose_name="Hometown")
    home_long = models.TextField(null=True, verbose_name="Hometown Longitude")
    home_lat = models.TextField(null=True, verbose_name="Hometown Latitude")
    high_school = models.CharField(null=True, max_length=140, verbose_name="High School")
    batting_avg = models.CharField(null=True, max_length=5)
    gp_gs = models.CharField(null=True, max_length=5)
    at_bats = models.CharField(null=True, max_length=5)
    runs = models.CharField(null=True, max_length=5)
    hits = models.CharField(null=True, max_length=5)
    doubles = models.CharField(null=True, max_length=5)
    homeruns = models.CharField(null=True, max_length=5)
    rbi = models.CharField(null=True, max_length=5)
    total_bases = models.CharField(null=True, max_length=5)
    slugging = models.CharField(null=True, max_length=5)
    walks = models.CharField(null=True, max_length=5)
    strikeouts = models.CharField(null=True, max_length=5)
    on_base_percentage = models.CharField(null=True, max_length=5)
    assists = models.CharField(null=True, max_length=5)
    errors = models.CharField(null=True, max_length=5)
    story = models.TextField(null=True)
    
    
    class Meta(object):
        ordering = ('name', 'position')
        
    def __unicode__(self):
        return U'%s' %(self.name)
    
    
    
class Coach(models.Model):
    name = models.TextField(null=True)
    
    class Meta(object):
        verbose_name_plural = "Coaches"
        ordering = ('name',)
    
    def __unicode__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.name = self.name()
        super(Player, self).save(*args, **kwargs)

    coachingage = models.CharField(null=True, max_length=2)
    college = models.TextField(null=True)
    gradyear = models.CharField(null=True, max_length=4)
    backstory = models.TextField(null=True)
    