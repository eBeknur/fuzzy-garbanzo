from django.contrib import admin
from .models import User , OTP , Market , Product , Rate , UserAddress , Order , Category

admin.site.register(User)
admin.site.register(OTP)
admin.site.register(Market)
admin.site.register(Product)
admin.site.register(Rate)
admin.site.register(UserAddress)
admin.site.register(Order)
admin.site.register(Category)

