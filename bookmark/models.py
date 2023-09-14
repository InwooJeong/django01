from django.db import models

# Create your models here.
class Bookmark(models.Model):   # django의 model 클래스를 상속
  # 필드 선언,    # blank 빈값 허용 여부, null 허용
  title = models.CharField(max_length=100,blank=True,null=True)
  # unique = pk
  url = models.URLField("url",unique=True)

  # 객체를 문자열로 표현하는 함수
  def __str__(self):
    return self.title