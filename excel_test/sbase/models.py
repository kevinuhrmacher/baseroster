import random
import sha
import datetime

from django.db import models
from django.contrib.localflavor.us.models import PhoneNumberField
from django.contrib.localflavor.us.us_states import STATE_CHOICES
from django.contrib.auth.models import User

from sbase.constants import *



TITLE_CHOICES = (
    ('Dr.', 'Dr.'),
    ('Mr.', 'Mr.'),
    ('Ms.', 'Ms.'),
    ('Mrs.', 'Mrs.'),
    ('Miss.', 'Miss.'),
)

USER_TYPE_CHOICES = (
    ('Administrator', 'Administrator'),
    ('Teacher', 'Teacher'),
    ('Parent', 'Parent'),
    ('Student', 'Student'),
)

GRADE_YEAR_CHOICES = (
    (-2, 'Toddler / Primary-1'),
    (-1, 'Pre-K / Primary-2'),
    (0, 'Kindergarten / Primary-3'),
    (1, '1st Grade / Lower Elementary-1'),
    (2, '2nd Grade / Lower Elementary-2'),
    (3, '3rd Grade / Lower Elementary-3'),
    (4, '4th Grade / Upper Elementary-4'),
    (5, '5th Grade / Upper Elementary-5'),
    (6, '6th Grade / Upper Elementary-6'),
    (7, '7th Grade / Middle School-7'),
    (8, '8th Grade / Middle School-8'),
    (9, '9th Grade / Middle School-9'),
)

MONTH_CHOICES = (
    ('1', 'January'),
    ('2', 'February'),
    ('3', 'March'),
    ('4', 'April'),
    ('5', 'May'),
    ('6', 'June'),
    ('7', 'July'),
    ('8', 'August'),
    ('9', 'September'),
    ('10', 'October'),
    ('11', 'November'),
    ('12', 'December'),
)

year_choices = [(str(year),str(year)) for year in range(1991, datetime.datetime.now().year)]


# Create your models here.
class School(models.Model):
    """Represents a school in schoolicity."""
    import_dict = { 
				'overrides':{},
				'object_colmap':{
					'identity_fields':['name','zip'],
					'self_field_cols':[1,6,7,10,12,13,2,3],
					'simple_related_cols':[],
					'field_col_mapping':{
						1:'name',
						6:'address_1',
						7:'city',
						10:'state',
						12:'zip',
						13:'phone',
						2:'email',
						3:'is_private',
					},
				},
			}
    export_dict = { 
				'object_export': ['name','address_1','address_2','city', \
								 'state','zip','phone', 'fax', 'email','is_private'],
			}
    name = models.CharField("Name of school", max_length=100)
    address_1 = models.CharField("Street address", max_length=200)
    address_2 = models.CharField("Suite, Box #, etc", max_length=200, blank=True, null=True)
    city = models.CharField("City", max_length=100)
    state = models.CharField("State", choices=STATE_CHOICES, max_length=100)
    zip = models.CharField("Zipcode", max_length=10)
    phone = PhoneNumberField("Phone number")
    fax = PhoneNumberField("Fax number", blank=True, null=True)
    email = models.EmailField("Email address")
    is_private = models.BooleanField("Is private?", default=False)
    id_key = models.CharField("Invite Key for School", max_length=40, blank=True, null=True)

    def __unicode__(self):
        return self.name + ' (' + self.city + ', ' + self.state + ')'

    def save(self, force_insert=False, force_update=False):
        if self.id_key is None:
            salt = sha.new(str(random.random())).hexdigest()[:5]
            self.id_key = sha.new(salt+self.name).hexdigest()
        super(School, self).save(force_insert, force_update) # Call the "real" save() method.

class Person(models.Model):
    """
    This is the Profile class for person entities in Schoolicity.
    
    It represents common characteristics among students, teachers,
    parents, and admins.
    
    While User objects may be created 'based' on a given parent or
    teacher, the Person class is maintained separately from the 
    Django User object.
    
    """
    title = models.CharField("Title", max_length=4, choices=TITLE_CHOICES)
    first_name = models.CharField("First name", max_length=100)
    last_name = models.CharField("Last name", max_length=100)
    address = models.CharField("Home street address", max_length=100)
    city = models.CharField("City", max_length=100)
    state = models.CharField("State", choices=STATE_CHOICES, max_length=100)
    zip = models.CharField("Zipcode", max_length=100)
    email = models.EmailField("Preferred email address")
    phone_primary = PhoneNumberField("Primary phone #")
    phone_secondary = PhoneNumberField("Secondary phone #", blank=True, null=True)
    invite_key = models.CharField("Last invitation code", max_length=50, blank=True, null=True)
    invite_datetime = models.DateTimeField("Last invitation date",blank=True, null=True)
    type = models.CharField("User type", max_length=15, choices=USER_TYPE_CHOICES, blank=True, null=True)
    
    school = models.ForeignKey(School, blank=True, null=True)
    user = models.ForeignKey(User, unique=True, blank=True, null=True)

    class Meta:
        ordering = ('last_name', 'first_name')

    def get_absolute_url(self):
        return ('profiles_profile_detail', (), { 'username': self.user.username })
    get_absolute_url = models.permalink(get_absolute_url)

#    def save(self, force_insert=False, force_update=False):
#        if self.user:
#            self.user.email = self.email
#            self.user.save()
#        super(Person, self).save(force_insert, force_update) # Call the "real" save() method.
        
    def type_as_number(self):
        return PERSON_TYPE_ID_DICT[self.type]
    
    def full_name(self):
        return self.first_name + ' ' + self.last_name

    def formal_name(self):
        if self.title:
            return self.title + ' ' + self.full_name()
        else:
            return self.full_name()

    def library_name(self):
        return self.last_name + ', ' + self.first_name

    def folder_name_for_person(self):
        return self.last_name + '_' + self.first_name + '_' + str(self.id)
		
    def __unicode__(self):
        return self.library_name()

def get_school_from_request(request):
    return '555-555-1212'

def get_date_from_string(request, date_string):
    return '555-555-1212'


class Parent(Person):
    """A parent in the schoolicity database."""
    import_dict = { 
				'overrides':{
					'type':'Parent',
					'phone_secondary':get_school_from_request,
				},
				'object_colmap':{
					'identity_fields':['first_name','last_name','email'],
					'self_field_cols':[0,1,2,3,4,5,6,7,8,9,10],
					'simple_related_cols':[11],
					'field_col_mapping':{
						0:'title',
						1:'first_name',
						2:'last_name',
						3:'address',
						4:'city',
						5:'state',
						6:'zip',
						7:'email',
						8:'phone_primary',
						9:'phone_secondary',
						10:'type',
						11:('school','sbase','School','name'),
					},
				},
				
			}

    export_dict = { 
				'object_export': ['title','first_name','last_name','address','city', \
								 'state','zip','email','phone_primary','phone_secondary','type', 'school'],
			}


class Student(Person):
    """A student in the schoolicity database."""
    import_dict = { 
				'overrides':{
					'type':'Student',
					#'dob':'2009-01-29',
					'phone_secondary':get_school_from_request,
				},
				'object_colmap':{
					'identity_fields':['first_name','last_name','email'],
					'self_field_cols':[0,1,2,3,4,5,6,7,8,9,10,11],
					'simple_related_cols':[12],
					'field_col_mapping':{
						0:'title',
						1:'first_name',
						2:'last_name',
						3:'address',
						4:'city',
						5:'state',
						6:'zip',
						7:'email',
						8:'type',
						9:'phone_primary',
						10:'phone_secondary',
						11:'dob',
						12:('school','sbase','School','name'),
					},
				},
				'relationship_colmap':{
					'parents':{
						'src_identity_cols':[0],
						'trg_identity_cols':[4],
						'src_col_mapping':{
							0:'id',
						},
						'trg_app':'sbase',
						'trg_model':'Parent',
						'trg_col_mapping':{
							4:'id',
						},
					},
				},
			}

    export_dict = { 
				'object_export': ['title','first_name','last_name','address','city', \
								 'state','zip','email','phone_primary','phone_secondary','type', 'dob', 'school'],
				'relationship_export':{
					'parents':{
						'self_fields':['id', 'first_name', 'last_name', 'phone_primary'],
						'related_fields':['id', 'first_name', 'last_name', 'email']
					},
				},
			}


    dob = models.DateField("Student's birth date", help_text='Used for determining age.')
    grade_year = models.IntegerField(choices=GRADE_YEAR_CHOICES, blank=True, null=True)
    parents = models.ManyToManyField(Parent, related_name="student_parent",blank=True, null=True)

    def __unicode__(self):
#        dob = self.dob
#        approx_age = datetime.datetime.today().date() - dob
        return self.last_name #+ ', ' + self.first_name + ' (age: ' + str(approx_age.days/365) + ')'

    
class Classroom(models.Model):
    """
    A class in the schoolicity database. A class can be held
    on different days.
    
    """
    name = models.CharField("Name of class", max_length=100)
    school = models.ForeignKey(School, blank=True, null=True)
    students = models.ManyToManyField(Student, related_name="classroom_student",blank=True, null=True)
    volunteers = models.ManyToManyField(Parent, related_name="classroom_parent",blank=True, null=True)
    group_email = models.EmailField("Group email list (Google Groups / Yahoo)")

    class Meta:
        ordering = ('name',)

    def __unicode__(self):
        return self.name

class Teacher(Person):
    """A teacher in the schoolicity database."""
    classrooms = models.ManyToManyField(Classroom, related_name="teacher_classroom",blank=True, null=True)