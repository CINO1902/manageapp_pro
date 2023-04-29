from django.contrib import admin

from .models import Event

from .models import ServiceType

from .models import ServiceUnit


admin.site.register(Event)

admin.site.register(ServiceType)

admin.site.register(ServiceUnit)
