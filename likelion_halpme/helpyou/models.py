from django.contrib.auth.models import AbstractUser
from django.db import models

# 회원가입
class CustomUser(AbstractUser):
    fullname = models.CharField(max_length=150)  # 사용자 이름
    year = models.CharField(max_length=4) # 생년월일-년도
    month = models.CharField(max_length=2) # 생년월일-월
    day = models.CharField(max_length=2) # 생년월일-일
    address = models.CharField(max_length=100) # 주소
    detailed_address = models.CharField(max_length=100) # 상세주소
    phone_number = models.CharField(max_length=13) # 전화번호
    email = models.EmailField(unique=True) # 이메일

    def __str__(self):
        return self.username
