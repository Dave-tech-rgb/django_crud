from django.shortcuts import render, redirect, get_object_or_404
from .models import Patient, Doctor, Appointment


def appointment_list(request):
    appointments = Appointment.objects.select_related('patient', 'doctor')
    return render(request, 'clinicapp/appointments.html', {
        'appointments': appointments
    })


def add_appointment(request):
    if request.method == "POST":

        patient_id = request.POST.get('patient')
        doctor_id = request.POST.get('doctor')

        new_patient = request.POST.get('new_patient')
        new_patient_age = request.POST.get('new_patient_age')

        new_doctor = request.POST.get('new_doctor')

        date = request.POST.get('date')
        time = request.POST.get('time')

        # -------- PATIENT --------
        if new_patient:
            try:
                age = int(new_patient_age)
            except (TypeError, ValueError):
                age = 0

            patient = Patient.objects.create(
                name=new_patient,
                age=age
            )
        else:
            patient = get_object_or_404(Patient, id=patient_id)

        # -------- DOCTOR --------
        if new_doctor:
            doctor = Doctor.objects.create(name=new_doctor)
        else:
            doctor = get_object_or_404(Doctor, id=doctor_id)

        # -------- APPOINTMENT --------
        Appointment.objects.create(
            patient=patient,
            doctor=doctor,
            date=date,
            time=time
        )

        return redirect('/')

    patients = Patient.objects.all()
    doctors = Doctor.objects.all()

    return render(request, 'clinicapp/add.html', {
        'patients': patients,
        'doctors': doctors
    })


def delete_appointment(request, id):
    appt = get_object_or_404(Appointment, id=id)
    appt.delete()
    return redirect('/')

def edit_appointment(request, id):

    appointment = get_object_or_404(Appointment, id=id)

    if request.method == "POST":

        patient_id = request.POST.get('patient')
        doctor_id = request.POST.get('doctor')

        date = request.POST.get('date')
        time = request.POST.get('time')

        appointment.patient = get_object_or_404(Patient, id=patient_id)
        appointment.doctor = get_object_or_404(Doctor, id=doctor_id)
        appointment.date = date
        appointment.time = time

        appointment.save()

        return redirect('/')

    patients = Patient.objects.all()
    doctors = Doctor.objects.all()

    return render(request, 'clinicapp/edit.html', {
        'appointment': appointment,
        'patients': patients,
        'doctors': doctors
    })
