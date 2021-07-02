from django.contrib import admin
from app.models import T_Users, T_Procedures


class T_UsersAdmin(admin.ModelAdmin):
    list_display = ['name', 'id', 'get_procedures_by_curator', ]
    readonly_fields = ('get_procedures_by_curator',)


class T_ProceduresAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'curator',
        'xml_type',
        'purchaseNumber',
        'docPublishDate',
        'purchaseObjectInfo',
        'regNum',
        'maxPrice',

    ]


admin.site.register(T_Users, T_UsersAdmin)
admin.site.register(T_Procedures, T_ProceduresAdmin)
