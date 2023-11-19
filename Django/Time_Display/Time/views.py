from django.shortcuts import render
from time import gmtime, strftime
import datetime
    
def index(request):
    now = datetime.datetime.now()
    times = now.strftime("%b %d, %Y %H:%M %p")
 
    context = {
        #"time": strftime("%Y-%m-%d %H:%M %p", gmtime())
        #"time": strftime("%b %d, %Y %H:%M %p", gmtime())
        'time': times
        
    }
    return render(request,'index.html', context)