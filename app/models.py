from django.db import models


class Book(models.Model):
    name = models.CharField(
        max_length=255,
        blank=True,
        null=True,
    )
    auther = models.CharField(
        max_length=255,
        blank=True,
        null=True,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Library(models.Model):
    book_id = models.ForeignKey(
        to=Book,
        on_delete=models.CASCADE,
        blank=True,
        null=False,
        default=0,
    )
    is_lent = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
