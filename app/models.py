from datetime import timedelta

from django.db import models
from ..user.models import CustomUserModel


# 書跡
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    isbn = models.CharField(max_length=13)
    available = models.BooleanField(default=True)

    def check_availability(self):
        return self.available


class Loan(models.Model):
    user = models.ForeignKey(
        to=CustomUserModel,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    book = models.ForeignKey(
        to=Book,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    loanDate = models.DateTimeField(
        verbose_name="貸し出し日",
        auto_now_add=True
    )
    dueDate = models.DateTimeField(
        verbose_name="返却期限",
    )

    def extendLoan(self, days=7):
        if self.dueDate:
            self.dueDate += timedelta(days=days)
            self.save()
