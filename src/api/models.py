from django.db import models
from django.conf import settings


# TODO check all fields and name models in the same way as in other services
class ClientProduct(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    id_product = models.IntegerField(null=False, blank=False)
    active = models.BooleanField(default=True)
    add_date = models.DateTimeField(auto_now_add=True)
    mod_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Client Products"

    def __str__(self):
        return f"Product: {self.id_product} of user: {self.user}"


class ClientExercise(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    id_exercise = models.IntegerField(null=False, blank=False)
    active = models.BooleanField(default=True)
    add_date = models.DateTimeField(auto_now_add=True)
    mod_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Client Exercises"

    def __str__(self):
        return f"Exercise: {self.id_exercise} of user: {self.user}"
