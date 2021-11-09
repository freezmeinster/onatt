from django.db import models

class AttendanceOffice(models.Model):
    name = models.CharField(max_length=255)
    longlat = models.CharField(max_length=255)
    min_radius = models.IntegerField(default=100)

    def __str__(self):
        return self.name

class AttendanceLog(models.Model):
    TYPE_IN = "I"
    TYPE_OUT = "O"
    TYPE = (
        (TYPE_IN, "IN"),
        (TYPE_OUT, "OUT"),
    )
    

    create_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    office = models.ForeignKey("attendance.AttendanceOffice",
            on_delete=models.CASCADE)
    type = models.CharField(choices=TYPE, default=TYPE_IN, max_length=1)

    def __str__(self):
        return self.user.username

class EmployeeAssignment(models.Model):
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    office = models.ForeignKey("attendance.AttendanceOffice",
            on_delete=models.CASCADE)
    active = models.BooleanField(default=True)

    class Meta:
        unique_together = ['user', 'office']
    
