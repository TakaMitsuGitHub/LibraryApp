from django.db import models
import csv
import numpy as np


class Book(models.Model):
    title = models.CharField(
        max_length=100,
        blank=True,
        null=False,
        default="",
    )
    auther = models.CharField(
        max_length=100,
        blank=True,
        null=False,
        default="",
    )
    aaa = models.CharField(
        max_length=100,
        blank=True,
        null=False,
        default="",
    )
    bbb = models.IntegerField(
        blank=True,
        null=False,
        default=0,
    )
    ccc = models.FloatField(
        blank=True,
        null=False,
        default=0,
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
    )

    @classmethod
    def from_csv_row(cls, row):
        """
        CSVの行からBookインスタンスを作成します。
        """
        return cls(
            title=row["タイトル"],
            auther=row["著者"]
        )



