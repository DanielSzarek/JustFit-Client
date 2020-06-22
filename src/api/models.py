from django.db import models
from django.conf import settings


class ClientProduct(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    id_product = models.IntegerField(null=False, blank=False)
    active = models.BooleanField(default=True)
    add_date = models.DateTimeField(auto_now_add=True)
    mod_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Client Products"
        indexes = [
            models.Index(fields=['user', "id_product", "active"], name='product_name_idx')
        ]

    def __str__(self):
        return f"Product: {self.id_product} of user: {self.user}"


class ClientActivity(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    id_activity = models.IntegerField(null=False, blank=False)
    active = models.BooleanField(default=True)
    add_date = models.DateTimeField(auto_now_add=True)
    mod_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Client Activities"
        indexes = [
            models.Index(fields=['user', "id_activity", "active"], name='activity_name_idx')
        ]

    def __str__(self):
        return f"Activity: {self.id_activity} of user: {self.user}"
