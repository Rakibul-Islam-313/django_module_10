from django.shortcuts import render
import datetime
# Create your views here.
def home(request):
    d = {'author':'rakib', 'age': 12,'lst': ['python','is','best'], 'birthday' : datetime.datetime.now(),'val': ' ','courses': [
        {
            'id': 1,
            'name': 'Python',
            'fee': 1500
        },
        {
            
            'id': 2,
            'name': 'C++',
            'fee': 1000
        }
    ]}
    return render(request,'home.html',context=d)