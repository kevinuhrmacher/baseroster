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
    weight = models.IntegerField(null=True, max_length=3, verbose_name="Weight")
    year = models.CharField(null=True, max_length=30)
    hometown = models.TextField(null=True, verbose_name="Hometown")
    high_school = models.CharField(null=True, max_length=140, verbose_name="High School")
    batting_avg = models.IntegerField(null=True)
    gp_gs = models.IntegerField(null=True)
    at_bats = models.IntegerField(null=True)
    runs = models.IntegerField(null=True)
    hits = models.IntegerField(null=True)
    doubles = models.IntegerField(null=True)
    homeruns = models.IntegerField(null=True)
    rbi = models.IntegerField(null=True)
    total_bases = models.IntegerField(null=True)
    slugging = models.IntegerField(null=True)
    walks = models.IntegerField(null=True)
    strikeouts = models.IntegerField(null=True)
    on_base_percentage = models.IntegerField(null=True)
    assists = models.IntegerField(null=True)
    errors = models.IntegerField(null=True)
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
    