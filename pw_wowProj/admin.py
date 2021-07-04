from django.contrib import admin

from pw_wowProj.models import Feedback,Contacto,Raid,Raider,raiddifficulty
# Register your models here.

admin.site.register(Feedback)
admin.site.register(Contacto)
admin.site.register(raiddifficulty)
admin.site.register(Raid)
admin.site.register(Raider)