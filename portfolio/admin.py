from django.contrib import admin
from . import models
# Register your models here.
class InfoAdmin(admin.ModelAdmin):
    list_display=('name','phone','age','city')

class SkillsAdmin(admin.ModelAdmin):
    list_display=('skill','perce')
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('skill','perce')}
        ),)
class PortfolioAdmin(admin.ModelAdmin):
    list_display=('titel','category','client','project_date',)
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('titel','category','client','project_date',)}
        ),)
    
class ServiceAdmin(admin.ModelAdmin):
    list_display=('name','description')
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('name','description','bootstrap_icon')}
        ),
    )
class MsgAdmin(admin.ModelAdmin):
    list_display=('name','email','subject','message')
    
class ProfileInline(admin.StackedInline):
    model = models.Images
    can_delete = False
    verbose_name_plural = 'Images'

admin.site.register(models.Portfolio,PortfolioAdmin)
admin.site.register(models.Info,InfoAdmin)
admin.site.register(models.Service,ServiceAdmin)
admin.site.register(models.Images)
admin.site.register(models.Message,MsgAdmin)
admin.site.register(models.Skills,SkillsAdmin)
