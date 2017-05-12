from django.contrib import admin
from models import *

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'nickname',)
    list_editable = ('username', 'email', 'nickname',)

class TeacherDisplay(admin.ModelAdmin):
    list_display = ('username', 'job_title')


admin.site.register(class_info)
admin.site.register(User, UserAdmin)
admin.site.register(Teacher, TeacherDisplay)
admin.site.register(Category)
admin.site.register(Plate)
admin.site.register(Article)
admin.site.register(Ad)
admin.site.register(Link)
admin.site.register(Strategic)


