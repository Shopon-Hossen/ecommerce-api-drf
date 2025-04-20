from django.urls import path
from . import views


urlpatterns = [
    path("list/", views.UserNotificationListView.as_view(), name="list_user_notification"),
    path("mark-read/", views.MarkIsReadUserNotificationView.as_view(), name="mark_read-user_notification"),
]