from django.contrib import admin
from .models import AttendanceOffice, AttendanceLog

@admin.register(AttendanceOffice)
class AttendnaceOfficeAdmin(admin.ModelAdmin):
    pass


@admin.register(AttendanceLog)
class AttendnaceLogAdmin(admin.ModelAdmin):
    list_display = ['user', 'office', 'type', 'create_date']
