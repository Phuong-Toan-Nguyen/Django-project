from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
from ckeditor.fields import RichTextField


# Create your models here.
class Menu_Items(models.Model):
    ItemName = models.CharField(max_length=20, null=False)
    Url = models.CharField( max_length=200,  null=True)

class Logo_pic(models.Model):
    Img = models.ImageField(upload_to='', null=True)
    alt = models.CharField( max_length=200, null=True)
    
class Carousel_Items(models.Model):
    Img = models.ImageField(upload_to='carousels/', null=True)
    description = models.CharField(max_length=200, null=True)
    alt = models.CharField( max_length=200, null=True)
    
class News_Items(models.Model):
    Title = models.CharField(max_length=100, null=True)
    ImgThumb = models.ImageField(upload_to='news/', null=True)
    VideoUrl = models.CharField(max_length=100, null=True, blank=True)
    UpdateAt = models.DateField(auto_now=True, )
    Content = RichTextField(blank = True, null = True)
    
class OnA_Items(models.Model):
    Title = models.CharField(max_length=20,)
    Date = models.DateField(null=True)
    Detail = models.CharField(max_length=20,)
    
class Story_Items(models.Model):
    ImgThumb = models.ImageField(upload_to='story/', null=True)
    Title = models.CharField(max_length=20, null=True)
    SubTitle = models.CharField(max_length=50, null=True)
    Content = models.CharField(max_length=500,)
    
class Donors(models.Model):
    Favicon = models.ImageField(upload_to='Donors/', null=True,)
    Url = models.CharField(max_length=100, null=True,)
    
class Staff_Cast(models.Model):
    Img = models.ImageField(upload_to='StaffCast/', null=True,)
    Name = models.CharField(max_length=30, null=True,)
    Url = models.CharField(max_length=100, null=True,)
    Movie = models.CharField(max_length=20, null=True,)
    job = models.CharField(max_length=20, null=True,)
    
class Trailer(models.Model):
    Img = models.ImageField(upload_to="Trailers/", null=True,)
    Name = models.CharField(max_length=30, null=True,)
    Url = models.CharField(max_length=100, null=True,)
    
class Music(models.Model):
    Img = models.ImageField(upload_to="Musics/", null=True,)
    Name = models.CharField(max_length=30, null=True,)
    Type = models.CharField(max_length=30, null=True,)
    Content = models.CharField(max_length=500, null=True,)
    
class BluDvD(models.Model):
    ImgThumb = models.ImageField(upload_to="BluDvD/", null=True,)
    ImgDetail = models.ImageField(upload_to="BluDvD/", null=True,)
    Name = models.CharField(max_length=20, null=True,)
    Content = models.CharField(max_length=500, null=True,)
    
class Goods(models.Model):
    Name = models.CharField(max_length=30, null=True,)
    Img = models.ImageField(upload_to="Goods/", null=True,)
    SellDate = models.CharField(max_length=30, null=True,)
    Price = models.CharField(max_length=30, null=True,)
    Category = models.CharField(max_length=20, null=True,)
    Description = models.CharField(max_length=200, null=True,)
    Url = models.CharField(max_length=100, null=True,)
    
class Podcast(models.Model):
    Name = models.CharField(max_length=30, null=True,)
    Img = models.ImageField(upload_to="Podcast/", null=True,)
    Url = models.CharField(max_length=100, null=True,)
    

    