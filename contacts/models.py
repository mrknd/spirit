from django.db import models


class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    car_id = models.IntegerField(blank=True, null=True)
    customer_need = models.CharField(max_length=100)
    car_title = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    message = models.TextField()
    user_id = models.IntegerField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} - {self.phone}"

