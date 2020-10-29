from django.contrib import admin
from .models import Dog, Walking, Toy

# Register your models here.
admin.site.register(Dog)
admin.site.register(Walking)
admin.site.register(Toy)