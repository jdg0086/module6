from django.contrib import admin

from .models import Branch, Agent, Transaction

admin.site.register(Branch)
admin.site.register(Agent)
admin.site.register(Transaction)