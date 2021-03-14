from django.contrib import admin
from django.apps import apps
from mainapp.models import *

admin.site.site_header = 'GYM STUDIO'
apps.get_app_config('mainapp').verbose_name = 'Абонементы'


@admin.register(Membership)
class MembershipAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'group',
        'price',
        'payment_period'
    )
    list_filter = (
        'group',
        'title',
        'payment_period'
    )
    list_editable = (
        'group',
        'price',
        'payment_period'
    )


@admin.register(MembershipGroup)
class MembershipGroupAdmin(admin.ModelAdmin):
    list_display = (
        'title',
    )


@admin.register(MembershipOptions)
class MembershipOptionsAdmin(admin.ModelAdmin):
    list_display = (
        'title',
    )


@admin.register(MembershipGroupOptions)
class MembershipGroupOptionsAdmin(admin.ModelAdmin):
    list_display = (
        'title',
    )


@admin.register(PromotionPrice)
class PromotionPriceAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'discount'
    )
    list_editable = (
        'discount',
    )
