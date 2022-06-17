from django.db import models
from django.contrib.auth.models import AbstractBaseUser


# Create your models here.
class UserType(models.Model):
    name = models.CharField("유저 타입", max_length=50)
    def __str__(self):
        return self.name

# custom user model    
class User(AbstractBaseUser):
    username = models.CharField("사용자 계정", max_length=50, unique=True)
    password = models.CharField("비밀번호", max_length=128)
    email = models.EmailField("이메일 주소", max_length=100)
    fullname = models.CharField("이름", max_length=20)
    join_date = models.DateField("가입일", auto_now_add=True)
    type = models.ManyToManyField(UserType, verbose_name="타입")

    is_active = models.BooleanField(default=True)

    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    
