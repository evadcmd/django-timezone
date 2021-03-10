from django.db import models

# Create your models here.
class Log(models.Model):

    server_saved_at = models.DateTimeField(
        verbose_name="サーバー保存日時",
        null=True,
        auto_now_add=True
    )

    browser_saved_at = models.DateTimeField(
        verbose_name="ブラウサ保存日時",
        null=True,
    )