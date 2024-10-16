from django.contrib import admin

from .models import Member

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ['id','firstname','lastname','phone','joined_date']