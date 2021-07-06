from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from .models import Credentials
from django.http import HttpResponseRedirect


# Create your views here.

def index(request):
    credential_items = Credentials.objects.all().order_by("-added_date")
    return render(request, 'main/index.html',{
        "credential_items" : credential_items
    })

@csrf_exempt
def add_credential(request):
    current_date = timezone.now()
    Name = request.POST["site"]
    Uid = request.POST["uid"]
    password = request.POST["password"]
    created_obj = Credentials.objects.create(added_date=current_date, 
                                      Site_Name = Name,
                                      UID = Uid,
                                      Password = password
    )
    return HttpResponseRedirect("/manager/")

@csrf_exempt
def delete_credential(request,credential_id):
    Credentials.objects.get(id=credential_id).delete()
    return HttpResponseRedirect("/manager/")
