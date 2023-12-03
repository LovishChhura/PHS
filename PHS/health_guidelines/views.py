from django.shortcuts import render,HttpResponse
from django.contrib.auth.decorators import login_required
import requests
from datetime import date
from datetime import timedelta

today = date.today() # or you can do today = date.today() for today's date
# today = date(2014, 10, 9)
weekdate=str(today-timedelta(days=7))

response=requests.get('https://newsapi.org/v2/top-headlines?country=in&category=health&from={weekdate}&sortBy=publishedAt&apiKey=<enter your api key>')

# Create your views here.
@login_required(login_url="/login/")
def index(request):
    mydict=response.json()
    article=[]
    for i in range(3):
        article1=mydict['articles'][i]
        author=article1['author']
        title=article1['title']
        desc=article1['description']
        dateofpub=article1['publishedAt'][:10]
        url=article1['url']
        urlImg=article1['urlToImage']
        art={'author':author,'title':title,'desc':desc,'dateofpub':dateofpub,'url':url,'urlImg':urlImg}
        article.append(art)
    return render(request,'health_guidelines.html',{'article':article})

