from django.contrib import admin

# Register your models here.
from .models import *

@admin.register(APPLIST)
class APPLISTeleAdmin(admin.ModelAdmin):
    list_display = ('id','title','Appclass','PANdomurl', 'star_time','last_time','isDelete')
    #筛选器
    list_filter =('isDelete','Appclass') #过滤器
    search_fields =('id', 'title') #搜索字段
    list_editable = ['Appclass','PANdomurl']   #list_editable 设置默认可编辑字段
    date_hierarchy = ('star_time')    # 详细时间分层筛选　

@admin.register(dynamic)
class dynamicTeleAdmin(admin.ModelAdmin):
    list_display = ('id','Classid','title','userID')
    search_fields =('id', 'title', 'userID') #搜索字段

    list_filter =('Classid', 'isDelete') #过滤器
    search_fields =('id', 'title', 'userID') #搜索字段
    date_hierarchy = ('star_time')   # 详细时间分层筛选　
    
@admin.register(TitleClassification)
class TitleClassificationTeleAdmin(admin.ModelAdmin):
    list_display = ('id','title')

@admin.register(warehouse)
class warehouseAdmin(admin.ModelAdmin):
    list_display = ('id','title','numbers')