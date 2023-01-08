from django.urls import path

from . import views

app_name = "quizzes"
urlpatterns = [
    path("", views.create, name="create"),
    path("<int:quiz_id>/thinking", views.thinking, name="thinking"),
    path("<int:quiz_id>/result/", views.result, name="result"),
]
