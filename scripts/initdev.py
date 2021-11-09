import os
from django.core.management import call_command
from django.contrib.auth.models import User
from attendance import models as att

def run():
    call_command("migrate")
    admin = User.objects.create_superuser(username="admin", password="admin")
    user1 = User.objects.create_user(username="user1", password="admin",
            is_staff=True)
    user2 = User.objects.create_user(username="user2", password="admin",
            is_staff=True)
    office1 = att.AttendanceOffice.objects.create(name="Politeknik LP3I Bandung",
            longlat="-6.896721033857478, 107.63391003311912")
    office2 = att.AttendanceOffice.objects.create(name="Politeknik LP3I Tasikmalaya",
            longlat="-7.32025448419668, 108.1986165265537")
    att.EmployeeAssignment.objects.create(user=user1, office=office1)
    att.EmployeeAssignment.objects.create(user=user2, office=office2)

