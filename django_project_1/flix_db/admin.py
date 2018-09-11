from django.contrib import admin
from .models import Like
from .models import Flix
from .models import User
# Register your models here.
admin.site.register(User)
admin.site.register(Flix)
admin.site.register(Like)