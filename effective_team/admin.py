from django.contrib import admin
from effective_team.models import Member


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    pass
