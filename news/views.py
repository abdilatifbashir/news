from django.shortcuts import render
from django.http import HttpResponse


import datetime as dt
#..........
def news_of_day(request):
    date = dt.date.today()
    html = "
        <html>
            <body>
                <h1> {date.day}-{date.month}-{date.year}</h1>
            </body>
        </html>"

    return HttpResponse(html)

# Create your views here.
