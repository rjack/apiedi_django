from django.db import models

VISIT_TYPES = (
	("v", "visita"),
	("c", "controllo di crescita"),
	("n", "neonato (prima visita)"),
	("C", "consulto"),
)

class Patient(models.Model):
	name = models.CharField(max_length=20)
	surname = models.CharField(max_length=20)
	telephone = models.CharField(max_length=20, blank=True, null=True)
	notes = models.CharField(max_length=500, blank=True, null=True)

	def __unicode__(self):
		return u"%s %s" % (self.name, self.surname)


class Appointment(models.Model):
	time = models.DateTimeField(primary_key=True)
	visitType = models.CharField(max_length=1, choices=VISIT_TYPES)
	patient = models.ForeignKey(Patient)
	notes = models.CharField(max_length=500, blank=True, null=True)

	def __unicode__(self):
		return u"%s,%s,%s" % (self.time, self.patient, self.visitType)
