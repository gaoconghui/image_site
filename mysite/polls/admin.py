from django.contrib import admin

# Register your models here.
from polls.models import Question

admin.site.register(Question)