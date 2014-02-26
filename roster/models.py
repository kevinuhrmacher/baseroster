from django.db import models

# Create your models here.

class Player(models.Model):
    name = models.CharField(max_length=50)
    
    class Meta(object):
        verbose_name_plural = "Players"
        ordering = ('name',)
    
    def __unicode__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.name = self.name.upper()
        super(Player, self).save(*args, **kwargs)

    backimageurl = models.TextField(null=True, max_length=200)
    imageurl = models.TextField(null=True, max_length=200)
    position = models.TextField(null=True)
    jerseyno = models.IntegerField(unique=True, null=True, max_length=2, verbose_name="No.")
    year = models.CharField(null=True, max_length=30)
    hometown = models.CharField(null=True, max_length=140, verbose_name="Hometown")
    highschool = models.CharField(null=True, max_length=140, verbose_name="High School")
    instaname =  models.TextField(null=True, verbose_name="Instagram User")
    major = models.TextField(null=True)
    backstory = models.TextField(null=True)
    
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
        self.name = self.name.upper()
        super(Player, self).save(*args, **kwargs)

    coachingage = models.CharField(null=True, max_length=2)
    college = models.TextField(null=True)
    gradyear = models.CharField(null=True, max_length=4)
    backstory = models.TextField(null=True)
    