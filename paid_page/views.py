from django.shortcuts import render
from paid_page.models import Harare_Students, Marondera_Students
# Create your views here.
def home(request):
    data = Harare_Students.objects.all()
    data1 = Marondera_Students.objects.all()
    return render(request, 'transportHome.html', {'data': data, 'data1': data1})

