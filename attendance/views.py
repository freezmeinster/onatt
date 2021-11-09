import ast
from geopy.distance import geodesic
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import AttendanceOffice, AttendanceLog

@login_required
def index(request):
    list_office = AttendanceOffice.objects.all()
    attend_type = "I"
    error = None
    if request.method == "POST":
        data = request.POST.copy()
        office = AttendanceOffice.objects.get(id=int(data['office']))
        base_office = ast.literal_eval(office.longlat)
        base_user = ast.literal_eval(data['latlong'])
        distance = geodesic(base_office,base_user).m
        if distance > 100:
            return redirect("error")
        else:
            AttendanceLog.objects.create(user=request.user, office=office, type=data['type'])
            return redirect("success")

    return render(request, "index.html", locals())

@login_required
def success(request):
    return render(request, "success.html")

@login_required
def error(request):
    return render(request, "error.html")
