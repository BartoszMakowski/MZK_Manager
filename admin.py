from django.contrib import admin

# Register your models here.

from .models import Przewoznicy, Autobusy, Kierowcy, Linie, Motorniczy
from .models import Odjazdy, Przejazdy, Przystanki, PunktyTrasy, Tramwaje, Zajezdnie

admin.site.register(Autobusy)
admin.site.register(Kierowcy)
admin.site.register(Linie)
admin.site.register(Motorniczy)
admin.site.register(Odjazdy)
admin.site.register(Przejazdy)
admin.site.register(Przewoznicy)
admin.site.register(PunktyTrasy)
admin.site.register(Tramwaje)
admin.site.register(Zajezdnie)
