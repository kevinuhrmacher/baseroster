from django.db import models

# Create your models here.

class Player(models.Model):
    number = models.IntegerField(unique=True, null=True, max_length=2, verbose_name="No.")
    lastname = models.CharField(max_length=50)
    firstname = models.CharField(max_length=50)
    
    class Meta(object):
        verbose_name_plural = "Players"
        ordering = ('number',)
    
    def __unicode__(self):
        return self.number
    
    def save(self, *args, **kwargs):
        self.lastname = self.lastname.upper()
        super(Player, self).save(*args, **kwargs)

    hand = models.CharField(null=True, max_length=5)
    position = models.TextField(null=True)
    height = models.CharField(null=True, max_length=3, verbose_name="Height")
    weight = models.IntegerField(null=True, max_length=3, verbose_name="Weight")
    year = models.CharField(null=True, max_length=30)
    hometown = models.CharField(null=True, max_length=140, verbose_name="Hometown")
    highschool = models.CharField(null=True, max_length=140, verbose_name="High School")
    story = models.TextField(null=True)
    
    
    class Meta(object):
        ordering = ('number', 'position')
        
    def __unicode__(self):
        return U'%s' %(self.number)
    
    
    
class Coach(models.Model):
    name = models.TextField(null=True)
    
    class Meta(object):
        verbose_name_plural = "Coaches"
        ordering = ('name',)
    
    def __unicode__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.name = self.name.upper()
        super(Player, self).save(*args, **kwargs)

    coachingage = models.CharField(null=True, max_length=2)
    college = models.TextField(null=True)
    gradyear = models.CharField(null=True, max_length=4)
    backstory = models.TextField(null=True)
    