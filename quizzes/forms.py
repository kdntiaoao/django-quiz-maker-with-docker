from django import forms

from .models import Quiz


class QuizForm(forms.ModelForm):
    class Meta:
        model = Quiz
        fields = (
            "statement",
            "option1",
            "option2",
            "option3",
            "option4",
            "option5",
            "is_option1_correct",
            "is_option2_correct",
            "is_option3_correct",
            "is_option4_correct",
            "is_option5_correct",
        )
