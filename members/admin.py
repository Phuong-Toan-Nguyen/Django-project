from django.contrib import admin
from .models import Menu_Items, Logo_pic, Carousel_Items, News_Items, OnA_Items, Story_Items, Donors, Staff_Cast, Trailer, Music, BluDvD, Goods, Podcast
# Register your models here.

class Menu_Items_Admin(admin.ModelAdmin):
    list_display = ("id","ItemName","Url")
admin.site.register(Menu_Items, Menu_Items_Admin)

class LogoAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
admin.site.register(Logo_pic, LogoAdmin)

class CarouselAdmin(admin.ModelAdmin):
    list_display = ("id", "Img", "description", "alt",)
admin.site.register(Carousel_Items,CarouselAdmin)

class NewsItemAdmin(admin.ModelAdmin):
    list_display = ("Title", "ImgThumb", "UpdateAt",)
admin.site.register(News_Items, NewsItemAdmin)

class OnAirItemAdmin(admin.ModelAdmin):
    list_display = ("Title", "Date", "Detail",)
admin.site.register(OnA_Items,OnAirItemAdmin)

class StoryItemAdmin(admin.ModelAdmin):
    list_display = ("Title", "ImgThumb", "SubTitle", "Content",)
admin.site.register(Story_Items,StoryItemAdmin)

class DonorAdmin(admin.ModelAdmin):
    list_display = ("id","Favicon", "Url",)
admin.site.register(Donors, DonorAdmin)

class StaffCastAdmin(admin.ModelAdmin):
    list_display = ("id", "Img", "Name", "Url", "Movie", "job",)
admin.site.register(Staff_Cast,StaffCastAdmin)

class TrailerAdmin(admin.ModelAdmin):
    list_display = ("id","Img", "Name", "Url",)
admin.site.register(Trailer,TrailerAdmin)

class MusicAdmin(admin.ModelAdmin):
    list_display = ("id", "Img", "Name", "Type", "Content",)
admin.site.register(Music, MusicAdmin)

class BluDvDAdmin(admin.ModelAdmin):
    list_display = ("id", "ImgThumb", "ImgDetail", "Name", "Content",)
admin.site.register(BluDvD,BluDvDAdmin)

class GoodsAdmin(admin.ModelAdmin):
    list_display = ("Name", "Img", "SellDate" , "Price", "Category", "Url",)
admin.site.register(Goods, GoodsAdmin)

class PodcastAdmin(admin.ModelAdmin):
    list_display = ("Name", "Img", "Url",)
admin.site.register(Podcast,PodcastAdmin)