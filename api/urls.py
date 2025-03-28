from django.urls import path, include

urlpatterns = [
    path('account/', include("account.urls")),
    path('shop/', include("shop.urls")),
    path('search/', include("search.urls")),
]
