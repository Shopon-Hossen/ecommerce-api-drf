from django.urls import path, include


urlpatterns = [
    path('product/', include("product.urls")),
    path('account/', include("account.urls")),
    path('shop/', include("shop.urls")),
    path('search/', include("search.urls")),
    path('cart/', include("cart.urls")),
    path('notification/', include("notification.urls")),
    path('chat/', include("chat.urls")),
    path('moderator/', include("moderator.urls")),
]
