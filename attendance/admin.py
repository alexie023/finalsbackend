from django.contrib import admin
from .models import Attendance

@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('student_name', 'course', 'date', 'status')
    list_filter = ('course', 'status', 'date')
    search_fields = ('student_name', 'course')
