from django.contrib import admin
from . models import feedback, order

admin.site.register(feedback)
admin.site.register(order)
feedback.objects.filter(name=None).delete()
order.objects.filter(name_o=None).delete()
