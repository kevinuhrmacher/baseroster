from django.contrib import admin
from batchadmin.admin import BatchModelAdmin
from models import School, Person, Parent, Classroom, Student, Teacher
from django.contrib.localflavor.us.forms import USPhoneNumberField
from django.contrib.localflavor.us.forms import USZipCodeField

class MyBatchAdmin(BatchModelAdmin):
    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name == "phone" or db_field.name == "phone_1" \
                or db_field.name == "phone_2" or db_field.name == "fax":
            return USPhoneNumberField(**kwargs)
        elif db_field.name == "zip":
            return USZipCodeField(**kwargs)
        return super(BatchModelAdmin,self).formfield_for_dbfield(db_field, **kwargs) 

admin.site.register(School, admin.ModelAdmin)
admin.site.register(Parent, admin.ModelAdmin)
admin.site.register(Person, admin.ModelAdmin)
admin.site.register(Classroom, admin.ModelAdmin)
admin.site.register(Student, admin.ModelAdmin)
admin.site.register(Teacher, admin.ModelAdmin)

