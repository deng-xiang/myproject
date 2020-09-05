from django.contrib import admin

# Register your models here.

from .models import Project

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id','name','types','create_time','close_time','status')
    #list_filter = ('create_time','status')
    search_fields = ('name','types')
    #fields = ('id','name','types','create_time','close_time','status')
    fieldsets = (
        (None, {
            'fileds':(
                'name',
                ('tpyes'),
                'status'
            )
        }),
    )


admin.site.register(Project)