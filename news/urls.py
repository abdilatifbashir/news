from django.conf.urls import url
from .import views

urlpatterns=[
    #......
    url('^today/$',views.news_of_day,name='newsToday')
]
