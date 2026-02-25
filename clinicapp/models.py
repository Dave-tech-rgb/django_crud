from django.db import models

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)

    def __str__(self):
        return f"Dr. {self.name}"

class Patient(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15, null=True, blank=True)

    def __str__(self):
        return self.name

class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    # Added null=True and blank=True to allow the database to 
    # populate existing rows during migration.
    date_time = models.DateTimeField(null=True, blank=True)
    reason = models.TextField(blank=True)

    def __str__(self):
        # Added a safety check for date_time in case it is None
        formatted_date = self.date_time.strftime('%Y-%m-%d %H:%M') if self.date_time else "No Date Set"
        return f"{self.patient.name} - {self.doctor.name} ({formatted_date})"