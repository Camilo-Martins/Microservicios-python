from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.core.validators import RegexValidator
from autoslug import AutoSlugField

# Create your models here.

User = get_user_model()
str_validator = RegexValidator(
    regex=r'^[a-zA-Z0-9]+$',
    message='Solo letras y números.'
)

class UserStore(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="stores"
    )
    token = models.CharField(max_length=100, 
                             blank=True, 
                             null=True)
    
    nombre_tienda = models.CharField(max_length=50, 
                                     blank=True, null=True, 
                                     validators=[str_validator],
                                     unique=True)
    slug = AutoSlugField(populate_from='nombre_tienda', 
                         null=True)

    def __str__(self):
        return f"{self.username}"
    

    class Meta:
        db_table     = "users_store"
        verbose_name = "UserStore"
        verbose_name_plural = "UsersStore"