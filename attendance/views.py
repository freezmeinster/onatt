import ast
from geopy.distance import geodesic
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import AttendanceOffice, AttendanceLog, EmployeeAssignment

@login_required
def index(request):
    list_office = EmployeeAssignment.objects.filter(user=request.user)
    attend_type = "I"
    last_log = AttendanceLog.objects.filter(user=request.user).order_by('create_date').last()
    if last_log and last_log.type == "I":
        attend_type = "O"
    if request.method == "POST":
        data = request.POST.copy()
        office = AttendanceOffice.objects.get(id=int(data['office']))
        base_office = ast.literal_eval(office.longlat)
        base_user = ast.literal_eval(data['latlong'])
        distance = geodesic(base_office,base_user).m
        if distance > office.min_radius:
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
