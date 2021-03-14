from django.contrib import admin

from django.apps import apps
from scheduleapp.models import *

apps.get_app_config('scheduleapp').verbose_name = 'Групповые занятия'


@admin.register(Trainer)
class TrainerAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )


@admin.register(WorkoutType)
class WorkoutTypeAdmin(admin.ModelAdmin):
    list_display = (
        'title',
    )


@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
    list_display = (
        'type',
        'trainer',
        'date',
        'start_workout',
        'workout_time',
    )
    list_editable = (
        'trainer',
        'date',
        'start_workout',
        'workout_time',
    )
    list_filter = (
        'type',
        'trainer',
        'date',
        'workout_time',
    )
    date_hierarchy = 'date'
