from django.conf import settings
from django.db import models


class Quiz(models.Model):
    statement = models.TextField("問題文")
    option1 = models.CharField("選択肢1", max_length=150)
    option2 = models.CharField("選択肢2", max_length=150)
    option3 = models.CharField("選択肢3", max_length=150)
    option4 = models.CharField("選択肢4", max_length=150)
    option5 = models.CharField("選択肢5", max_length=150)
    is_option1_correct = models.BooleanField("選択肢1は正解か", default=False)
    is_option2_correct = models.BooleanField("選択肢2は正解か", default=False)
    is_option3_correct = models.BooleanField("選択肢3は正解か", default=False)
    is_option4_correct = models.BooleanField("選択肢4は正解か", default=False)
    is_option5_correct = models.BooleanField("選択肢5は正解か", default=False)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, verbose_name="作成者", on_delete=models.CASCADE
    )
    created_at = models.DateTimeField("作成日", auto_now_add=True)
    updated_at = models.DateTimeField("更新日", auto_now=True)

    def __str__(self):
        return self.statement
