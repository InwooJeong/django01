from django.shortcuts import render
from bookmark.models import Bookmark
from django.views.generic import ListView, DetailView

# Create your views here.
def home(request):
  # SELECT * FROM bookmark_bookmark order by title
  urlList = Bookmark.objects.order_by("title")

  # SELECT COUNT(*) FROM bookmark_bookmark
  urlCount = Bookmark.objects.all().count()
  print(urlList)
  print(urlCount)
  # list.html 페이지로 넘어가서 출력
  # render("url",{"변수명":값,"변수명":값})
  return render(request,"bookmark/list.html",
                {"urlList":urlList,"urlCount":urlCount})

def detail(request):
  addr = request.GET["url"]
  dto = Bookmark.objects.get(url=addr)
  return render(request,"bookmark/detail.html",{"dto":dto})

# --- ListView 템플릿 파일 : 모델명소문자_list.html
class BookmarkLV(ListView):
  model = Bookmark

#--- DetailView
# 템플릿파일 : 모델명소물자_detail.html
class BookmarkDV(DetailView):
  model = Bookmark
