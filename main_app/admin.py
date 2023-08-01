from django.contrib import admin
from .models import Dog, ReportCard, Treat

# Register your models here.
admin.site.register(Dog)
admin.site.register(ReportCard)
admin.site.register(Treat)