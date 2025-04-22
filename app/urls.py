from django.urls import path
from .views import (
    registration, verify, resend, change_password,
    market_create, product_create, rate_create,
    user_address_create, order_create, category_create,
    market_put_update, market_patch_update,
    product_put_update, product_patch_update,
    rate_put_update, rate_patch_update,
    user_address_put_update, user_address_patch_update,
    order_put_update, order_patch_update,
    category_put_update, category_patch_update,
    market_delete, product_delete, rate_delete,
    user_address_delete, order_delete, category_delete,
)

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path("signup/", registration),
    path("verify/", verify),
    path("resend/", resend),
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("change-password/", change_password),

    path("create-market/", market_create),
    path("create-product/", product_create),
    path("create-rate/", rate_create),
    path("create-address/", user_address_create),
    path("create-order/", order_create),
    path("create-category/", category_create),

    path("market/<int:pk>/put/", market_put_update),
    path("market/<int:pk>/patch/", market_patch_update),

    path("product/<int:pk>/put/", product_put_update),
    path("product/<int:pk>/patch/", product_patch_update),

    path("rate/<int:pk>/put/", rate_put_update),
    path("rate/<int:pk>/patch/", rate_patch_update),

    path("user-address/<int:pk>/put/", user_address_put_update),
    path("user-address/<int:pk>/patch/", user_address_patch_update),

    path("order/<int:pk>/put/", order_put_update),
    path("order/<int:pk>/patch/", order_patch_update),

    path("category/<int:pk>/put/", category_put_update),
    path("category/<int:pk>/patch/", category_patch_update),

    path("market/<int:pk>/delete/", market_delete),
    path("product/<int:pk>/delete/", product_delete),
    path("rate/<int:pk>/delete/", rate_delete),
    path("user-address/<int:pk>/delete/", user_address_delete),
    path("order/<int:pk>/delete/", order_delete),
    path("category/<int:pk>/delete/", category_delete),
]
