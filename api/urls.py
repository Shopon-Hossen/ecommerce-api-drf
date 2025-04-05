from django.urls import path, include

urlpatterns = [
    path('product/', include("product.urls")),
    path('account/', include("account.urls")),
    path('shop/', include("shop.urls")),
    path('search/', include("search.urls")),
    path('review/shop/', include("shop_review.urls")),
    ]
