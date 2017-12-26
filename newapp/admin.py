#-*- coding: UTF-8 -*-
from django.contrib import admin
from .models import UserInfoFormModel,HighSchoolFormModel
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ( 'cell_phone_number','full_name','graduate_school','result_desc',
                     'intention_country1','intention_school','intention_major')  # list
    #list_editable = ('graduate_school',)
    list_per_page=12;
    search_fields = ('first_name','last_name','graduate_school','intention_country','intention_school',)
    #radio_fields = {'graduate_school': admin.VERTICAL}
    readonly_fields = ('first_name','last_name','graduate_school','cell_phone_number','graduate_school',
                       'ranking_in_major', 'score_GPA','intention_country','intention_school','intention_major',
                       'score_IELTS_TOEFL', 'score_IT_Listening', 'score_IT_Speaking', 'score_IT_Reading',
                       'score_IT_Writing',
                       'score_GRE', 'score_GRE_Quan', 'score_GRE_Verbal', 'score_GRE_Anal',
                       'in_papers', 'na_papers', 'in_patent', 'na_patent',
                       'research', 'placement', 'social_practice', 'specilty',
                       )
    fieldsets = (
        [u'个人信息', {
           # 'description':u'测试',
            'fields': ('first_name', 'last_name','cell_phone_number'),
        }],
        [u'教育背景', {
            'fields': ('graduate_school','ranking_in_major', 'score_GPA',),
        }],
        [u'留学意向', {
            'fields': ('intention_country','intention_school','intention_major',),
        }],
        [u'语言成绩', {
            'fields': ('score_IELTS_TOEFL', 'score_IT_Listening', 'score_IT_Speaking', 'score_IT_Reading', 'score_IT_Writing',
                        'score_GRE','score_GRE_Quan','score_GRE_Verbal','score_GRE_Anal',
                       ),
        }],
        [u'其他', {
            'classes': ('collapse',),
            'fields': (
                        'in_papers', 'na_papers', 'in_patent', 'na_patent',
                         'research', 'placement', 'social_practice', 'specilty',
            ),
        }],
    )

    def cell_phone_number(self,obj):
        return obj.cell_phone_number

    def graduate_school(self, obj):
        return obj.graduate_school

    def result_desc(self, obj):
        return obj.result_desc

    def intention_school(self,obj):
        return obj.intention_school

    def intention_major(self,obj):
        return obj.intention_major


    cell_phone_number.short_description = u"用户"
    graduate_school.short_description = u'毕业院校'
    result_desc.short_description = u'测评结果'
    intention_school.short_description = u'目标院校'
    intention_major.short_description = u'目标专业'


    def has_add_permission(self,request,obj=None):
         return False;
    def has_view_permission(self,request,obj=None):
        return True;
    def has_change_permission(self,request,obj=None):
          return True;
    def has_delete_permission(self,request,obj=None):
        return True;
admin.site.register(UserInfoFormModel,UserAdmin)

class HighShoolAdmin(admin.ModelAdmin):
    list_display = ( 'cell_phone_number','full_name','graduate_school',
                     'intention_country','intention_school','talentStudent',)  # list
    #list_editable = ('graduate_school',)
    list_per_page=12;
    search_fields = ('first_name','last_name','graduate_school','intention_country','intention_school',)
    #radio_fields = {'graduate_school': admin.VERTICAL}

    readonly_fields = ('first_name', 'last_name', 'cell_phone_number', 'graduate_school',
                       'GPA_high', 'GPA_middle','intention_country', 'intention_school',
                       'score_TOEFL', 'score_SAT',
                       'research', 'art', 'awards', 'recommendations','talentStudent',
                       )

    fieldsets = (
        [u'个人信息', {
           # 'description':u'测试',
            'fields': ('first_name', 'last_name','cell_phone_number'),
        }],
        [u'教育背景', {
            'fields': ('graduate_school','GPA_high', 'GPA_middle',),
        }],
        [u'留学意向', {
            'fields': ('intention_country','intention_school',),
        }],
        [u'语言成绩', {
            'fields': ('score_TOEFL','score_SAT',
                       ),
        }],
        [u'其他', {
            'fields': (
                        'talentStudent','research', 'art', 'awards', 'recommendations',
            ),
        }],
    )




    def has_add_permission(self,request,obj=None):
         return False;
    def has_view_permission(self,request,obj=None):
        return True;
    def has_change_permission(self,request,obj=None):
          return True;
    def has_delete_permission(self,request,obj=None):
        return True;
admin.site.register(HighSchoolFormModel,HighShoolAdmin)