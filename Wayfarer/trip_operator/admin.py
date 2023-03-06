from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Operator)
admin.site.register(OperatorUser)
admin.site.register(Trip)
admin.site.register(TripInstance)
admin.site.register(Category)


