from django.conf.urls.defaults import *

urlpatterns = patterns('apiedi_django.apiedi.views',
	(r"^appointments/$", "appointments"),
	(r"^appointments/new$", "new_appointment"),
)
