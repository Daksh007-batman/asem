from django.contrib import admin
from .models import User
from .models import Site, HomeGatewayId, AisleGroup


admin.site.register(User)
admin.site.register(Site)
admin.site.register(HomeGatewayId)
admin.site.register(AisleGroup)