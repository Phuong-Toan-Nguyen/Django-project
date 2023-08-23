#from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Menu_Items, Logo_pic, Carousel_Items, News_Items, OnA_Items, Story_Items, Donors, Staff_Cast, Trailer, Music, BluDvD, Goods, Podcast


# Create your views here.

def main(request):
    menuitems = Menu_Items.objects.all().values()
    favicon = Logo_pic.objects.get(id=1)
    donors = Donors.objects.all()
    carousels = Carousel_Items.objects.all() #truy van .url phai de object
    newsItems = News_Items.objects.all().order_by('-id')
    OnAirItems = OnA_Items.objects.all().order_by('-id')
    StoryItems = Story_Items.objects.all().order_by('-id')
    StaffCast = Staff_Cast.objects.all().order_by('-id')
    trailer = Trailer.objects.all().order_by('-id')
    music = Music.objects.all().order_by('-id')
    bludvd = BluDvD.objects.all().order_by('-id')
    goods = Goods.objects.all().order_by('-id')
    podcast = Podcast.objects.all().order_by('-id')
    template = loader.get_template('mainpage.html')
    context = {
        'items': menuitems,
        'favicon': favicon,
        'donors': donors,
        'carousels': carousels,
        'newsItems': newsItems,
        'OnAirItems': OnAirItems,
        'StoryItems': StoryItems,
        'StaffCast': StaffCast,
        'trailers': trailer,
        'musics': music,
        'bludvds': bludvd,
        'goods': goods,
        'podcasts': podcast,
    }
    return HttpResponse(template.render(context, request))

def testing(request):
    menuitems = Menu_Items.objects.all().values()
    favicon = Logo_pic.objects.get(id=1)
    carousels = Carousel_Items.objects.all() #truy van .url phai de object
    newsItems = News_Items.objects.all().order_by('-id')
    OnAirItems = OnA_Items.objects.all().order_by('-id')
    StoryItems = Story_Items.objects.all().order_by('-id')
    template = loader.get_template('testpage.html')
    context = {
        'items': menuitems,
        'favicon': favicon,
        'carousels': carousels,
        'newsItems': newsItems,
        'OnAirItems': OnAirItems,
        'StoryItems': StoryItems,
    }
    return HttpResponse(template.render(context, request))

def NewsDetail(request, id):
    newsItems = News_Items.objects.get(id=id)
    menuitems = Menu_Items.objects.all().values()
    favicon = Logo_pic.objects.get(id=1)
    donors = Donors.objects.all()
    template = loader.get_template('NewsDetail.html')
    context = {
        'newsItems': newsItems,
        'items': menuitems,
        'favicon': favicon,
        'donors': donors,
    }
    return HttpResponse(template.render(context, request))

def StoryDetail(request, id):
    storyItems = Story_Items.objects.get(id=id)
    menuitems = Menu_Items.objects.all().values()
    favicon = Logo_pic.objects.get(id=1)
    donors = Donors.objects.all()
    template = loader.get_template('StoryDetail.html')
    context = {
        'storys': storyItems,
        'items': menuitems,
        'favicon': favicon,
        'donors': donors,
    }
    return HttpResponse(template.render(context, request))

def TrailerDetail(request, id):
    trailer = Trailer.objects.get(id=id)
    menuitems = Menu_Items.objects.all().values()
    favicon = Logo_pic.objects.get(id=1)
    donors = Donors.objects.all()
    template = loader.get_template('TrailerDetail.html')
    context = {
        'items': menuitems,
        'favicon': favicon,
        'donors': donors,
        'trailers': trailer,
    }
    return HttpResponse(template.render(context, request))

def MusicDetail(request, id):
    music = Music.objects.get(id=id)
    menuitems = Menu_Items.objects.all().values()
    favicon = Logo_pic.objects.get(id=1)
    donors = Donors.objects.all()
    template = loader.get_template('MusicDetail.html')
    context = {
        'items': menuitems,
        'favicon': favicon,
        'donors': donors,
        'musics': music,
    }
    return HttpResponse(template.render(context, request))

def BludvdDetail(request, id):
    bludvd = BluDvD.objects.get(id=id)
    menuitems = Menu_Items.objects.all().values()
    favicon = Logo_pic.objects.get(id=1)
    donors = Donors.objects.all()
    template = loader.get_template('BludvdDetail.html')
    context = {
        'items': menuitems,
        'favicon': favicon,
        'donors': donors,
        'bludvds': bludvd,
    }
    return HttpResponse(template.render(context, request))

def GoodsDetail(request, id):
    goods = Goods.objects.get(id=id)
    template = loader.get_template('GoodsDetail.html')
    context = {
        'goods': goods
    }
    return HttpResponse(template.render(context, request))
