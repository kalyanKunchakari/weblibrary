from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import *
# Register your models here.

class StudentInline(admin.StackedInline):
    model = Student
    can_delete = False
    verbose_name_plural = 'Student'
    fk_name = 'user'

class CustomUserAdmin(UserAdmin):
    inlines = (StudentInline, )

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)

#admin.site.register(User)
#admin.site.register(User, CustomUserAdmin)
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(BookMainCategory)
admin.site.register(BookSubCategory)
admin.site.register(StudentMainTable)
admin.site.register(Student)