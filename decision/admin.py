from django.contrib import admin

from .models import Decision, Point, Discussion


class PointInline(admin.TabularInline):
    model = Point

class DecisionAdmin(admin.ModelAdmin):
    inlines = [PointInline]

admin.site.register(Decision,DecisionAdmin)

admin.site.register(Discussion)
