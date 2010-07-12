from django.template import Context, loader
from django.http import HttpResponse
from models import Appointment

def appointments(req):
	appointments = Appointment.objects.all().order_by("time");
	template = loader.get_template("appointments.html")
	context = Context({
		"appointments": appointments
	})
	return HttpResponse(template.render(context))


def new_appointment(req):
	return HttpResponse("Nuovo appuntamento! Deve essere un POST.")
