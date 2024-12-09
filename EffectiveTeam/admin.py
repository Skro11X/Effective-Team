from django.contrib import admin
from EffectiveTeam.models import Member


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    pass
