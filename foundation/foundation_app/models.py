from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('user', 'User'),
        ('manager', 'Manager'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='user')

    def is_manager(self):
        return self.role == 'manager'


class Request(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('needs_clarification', 'Needs Clarification'),
        ('denied', 'Denied'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255, verbose_name="ПІБ")
    military_unit_number = models.CharField(max_length=100, verbose_name="Номер військової частини")
    phone_number = models.CharField(max_length=20, verbose_name="Номер телефону")
    commander_name = models.CharField(max_length=255, verbose_name="ПІБ командира")
    request_text = models.TextField(verbose_name="Запит")
    comment = models.TextField(blank=True, null=True, verbose_name="Коментар")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    manager_comment = models.TextField(blank=True, null=True, verbose_name="Коментар менеджера")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Request by {self.full_name} - {self.status}"