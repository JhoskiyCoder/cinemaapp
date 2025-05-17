from django.contrib import admin
from .models import Movie, Session, Viewer, Ticket

admin.site.register(Movie)
admin.site.register(Session)
admin.site.register(Viewer)
admin.site.register(Ticket)

# Register your models here.
