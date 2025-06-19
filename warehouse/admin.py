from django.contrib import admin
from .models import User
from .models import Site, HomeGatewayId, AisleGroup, aisle_blocks, lights


admin.site.register(User)
admin.site.register(Site)
admin.site.register(HomeGatewayId)
admin.site.register(AisleGroup)
admin.site.register(aisle_blocks)
admin.site.register(lights)