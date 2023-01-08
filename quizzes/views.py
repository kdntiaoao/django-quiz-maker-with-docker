import math

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.template.response import TemplateResponse
from django.urls import reverse
from django.views.generic import View

from .forms import QuizForm
from .models import Quiz


class IndexView(View):
    def get(self, request, *args, **kwargs):
        total_count = Quiz.objects.select_related("created_by").all().count()
        total_page = math.ceil(total_count / 10)
        current_page = int(
            request.GET.get("current") if request.GET.get("current") else 1
        )
        quizzes = (
            Quiz.objects.select_related("created_by")
            .order_by("-updated_at")
            .all()[(current_page - 1) * 10 : current_page * 10]
        )
        return TemplateResponse(
            request,
            "quizzes/index.html",
            {
                "quizzes": quizzes,
                "total_count": total_count,
                "total_page": total_page,
                "current_page": current_page,
            },
        )


index = IndexView.as_view()


class ThinkingView(View):
    def get(self, request, quiz_id, *args, **kwargs):
        quiz = get_object_or_404(Quiz, pk=quiz_id)
        formatted_quiz = {
            "statement": quiz.statement,
            "options": [
                {
                    "text": quiz.option1,
                    "name": "option1",
                    "is_correct": quiz.is_option1_correct,
                },
                {
                    "text": quiz.option2,
                    "name": "option2",
                    "is_correct": quiz.is_option2_correct,
                },
                {
                    "text": quiz.option3,
                    "name": "option3",
                    "is_correct": quiz.is_option3_correct,
                },
                {
                    "text": quiz.option4,
                    "name": "option4",
                    "is_correct": quiz.is_option4_correct,
                },
                {
                    "text": quiz.option5,
                    "name": "option5",
                    "is_correct": quiz.is_option5_correct,
                },
            ],
            "created_by": quiz.created_by,
            "created_at": quiz.created_at,
            "updated_at": quiz.updated_at,
        }
        return TemplateResponse(
            request, "quizzes/thinking.html", {"quiz": formatted_quiz}
        )

    def post(self, request, quiz_id, *args, **kwargs):
        selected_answers = [
            request.POST.get("option1"),
            request.POST.get("option2"),
            request.POST.get("option3"),
            request.POST.get("option4"),
            request.POST.get("option5"),
        ]
        selects = ",".join(
            [str(i + 1) for i, x in enumerate(selected_answers) if x == "on"]
        )
        url = (
            reverse("quizzes:result", kwargs={"quiz_id": quiz_id})
            + "?selects="
            + selects
        )
        return HttpResponseRedirect(url)


thinking = ThinkingView.as_view()


class ResultView(View):
    def get(self, request, quiz_id, *args, **kwargs):
        quiz = get_object_or_404(Quiz, pk=quiz_id)
        selects = request.GET.get("selects").split(",")
        formatted_quiz = {
            "statement": quiz.statement,
            "options": [
                {
                    "text": quiz.option1,
                    "name": "option1",
                    "is_correct": quiz.is_option1_correct,
                    "is_select": "1" in selects,
                },
                {
                    "text": quiz.option2,
                    "name": "option2",
                    "is_correct": quiz.is_option2_correct,
                    "is_select": "2" in selects,
                },
                {
                    "text": quiz.option3,
                    "name": "option3",
                    "is_correct": quiz.is_option3_correct,
                    "is_select": "3" in selects,
                },
                {
                    "text": quiz.option4,
                    "name": "option4",
                    "is_correct": quiz.is_option4_correct,
                    "is_select": "4" in selects,
                },
                {
                    "text": quiz.option5,
                    "name": "option5",
                    "is_correct": quiz.is_option5_correct,
                    "is_select": "5" in selects,
                },
            ],
            "created_by": quiz.created_by,
            "created_at": quiz.created_at,
            "updated_at": quiz.updated_at,
        }
        return TemplateResponse(
            request, "quizzes/result.html", {"quiz": formatted_quiz}
        )


result = ResultView.as_view()


class QuizCreateView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        form = QuizForm()
        return TemplateResponse(request, "quizzes/create.html", {"form": form})

    def post(self, request, *args, **kwargs):
        form = QuizForm(request.POST)
        if not form.is_valid():
            print(form.errors)
            return TemplateResponse(request, "quizzes/create.html", {"form": form})
        quiz = form.save(commit=False)
        quiz.created_by = request.user
        quiz.save()
        return HttpResponseRedirect(reverse("index"))


create = QuizCreateView.as_view()
