from django.db import close_old_connections
from django.contrib import admin

from .models import Question


close_old_connections()
# Register your models here.
admin.site.register(Question)
