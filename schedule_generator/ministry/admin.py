from django.contrib import admin

from .models import Ministry, MinistryType, Member, MinistryActivity


class MinistryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    filter_horizontal = ('members',)

    def name(self, obj: Ministry):
        return MinistryType.get_type_name(obj.type)
    name.short_description = 'Nome'


class MinistryActivityAdmin(admin.ModelAdmin):
    list_display = ('activity', 'ministry')
    list_filter = ('ministry',)
    search_fields = ('activity', 'ministry__name')


class MemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active', 'ministries')
    filter_horizontal = ('activities',)

    def name(self, obj: Member):
        return obj.user.username
    name.short_description = 'Nome'

    def ministries(self, obj: Member):
        return ', '.join([m.__str__() for m in obj.ministry_members.all()])
    ministries.short_description = 'Ministérios'
    

admin.site.register(Ministry, MinistryAdmin)
admin.site.register(MinistryActivity, MinistryActivityAdmin)
admin.site.register(Member, MemberAdmin)