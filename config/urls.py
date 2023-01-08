from django.contrib import admin
from django.urls import include, path

from quizzes.views import index


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index, name="index"),
    path("accounts/", include("accounts.urls")),
    path("quizzes/", include("quizzes.urls")),
]
