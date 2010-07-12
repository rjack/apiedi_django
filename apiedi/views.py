from django.http import HttpResponse

def appointments(req):
	return HttpResponse("Tutti gli appuntamenti")


def new_appointment(req):
	return HttpResponse("Nuovo appuntamento! Deve essere un POST.")
