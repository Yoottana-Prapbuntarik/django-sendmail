from django.db import models

class Send_email(models.Model) :
    first_name  = models.CharField(max_length=100)
    for_send_email = models.EmailField(max_length=254)

def __str__(self):
        return self.first_name

