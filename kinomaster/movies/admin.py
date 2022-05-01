from django.contrib import admin
from .models import *

admin.site.register(Category)
admin.site.register(ActorsDirectors)
admin.site.register(Genre)
admin.site.register(Movies)
admin.site.register(RatingStar)
admin.site.register(Rating)
admin.site.register(Reviews)

