from django.contrib import admin
from django.urls import path, include

from feedbacks.api.urls import router

urlpatterns = [
    path("admin/", admin.site.urls),
    path("auth/", include("authentication.urls"), name="auth"),
    path("users/", include("users.urls"), name="users"),
    path("", include(router.urls), name="feedbacks"),
]
