from django.contrib import admin
from .models import StudentData
from .models import AdminData
from .models import Resources
from .models import Clubs
from .models import Event
from .models import Placements

# Register your models here.
admin.site.register(StudentData)
admin.site.register(AdminData)
admin.site.register(Resources)
admin.site.register(Clubs)
admin.site.register(Event)
admin.site.register(Placements)
