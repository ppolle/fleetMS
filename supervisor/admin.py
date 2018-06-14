from django.contrib import admin

from .models import Crew, Issue, Message, Supervisor

# Register your models here.
admin.site.register(Supervisor)
admin.site.register(Crew)
admin.site.register(Issue)
admin.site.register(Message)
