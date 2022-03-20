from django.db import models

class News(models.Model):
    cover = models.CharField(
        verbose_name='Cover',
        max_length=255,
    )

    title = models.CharField(
        verbose_name='Ritle',
        max_length=255,
    )


    resume = models.CharField(
        verbose_name='Resume',
        max_length=255,
    )


    text = models.CharField(
        verbose_name='Text',
        max_length=5000,
    )


    def __str__(self):
        return self.title


    class Meta:
        app_label = 'news'
        verbose_name = 'News'
        verbose_name_plural = 'News'