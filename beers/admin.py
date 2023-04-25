from django.contrib import admin
from .models import Brewery, Beer, Style, Malt


admin.site.register(Brewery)
admin.site.register(Beer)
admin.site.register(Style)
admin.site.register(Malt)
