from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import AttendanceOffice, AttendanceLog

@login_required
def index(request):
    list_office = AttendanceOffice.objects.all()
    if request.method == "POST":
        data = request.POST.copy()


    return render(request, "index.html", locals())
