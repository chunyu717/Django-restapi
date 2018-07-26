
前至步驟
pip install pipenv
Note : pipenv 的優點包括但不限於以下幾個：
	1. 會在專案以外的地方放置專案所需的套件．
	2. 自動管理套件之間的 dependency ，方便移除套件．例如安裝 pyspark 時會需要一併安裝 py4j ，如果單純使用 pip 安裝，雖然可以一併安裝，但是用 pip uninstall 移除時需要一個一個移除．這點在 pipenv 會幫忙管理，自動移除相關的 lib．
	3. 可以區分 dev 環境的套件，在安裝時可以選擇要不要包含 dev 環境的套件．就可以保持 prod 套件的乾淨
	4. 不需要使用 activate 或 deactivate 來切換環境．pipenv 可以使用 pipenv run 來直接使用虛擬環境提供的 lib．
	如果對於以上優點有興趣的可以來試著用用看 pyenv．

Getting Started With Django REST Framewore
https://www.youtube.com/watch?v=263xt_4mBNc&t=0s&list=WL&index=9

#安裝 framwaork
mkdir -p django-REST
cd dango-REST\
pipenv install djangorestframework

# 啟動虛擬環境
pipenv shell

#django-admin startproject api_example



# migrate 現存的 model ... user stuff
cd api_example
python manage.py migrate	//本地會多了一個檔案 db.sqlite3 

#建立 superuser
python manage.py createsuperuser

python manage.py startapp languages


#  api_example\api_example\settings.py 加入
INSTALLED_APPS = [
	'rest_framework',
	'languages',
]

#以上設定完成

#  api_example\api_example\urls.py 加入
urlpatterns = [
	path('', incloude('languages.urls')
]

# 新增 api_example\laguages\urls.py 
from django.urls import path, include 
from . import views
urlpatterns = [
    
]

# 編輯 model.py

class Language(models.Model):
	name = models.CharField(max_length=50)
	paradigm= models.CharField(max_length=50)

#建立 model language
$python manage.py makemigrations

#apply model language => 至此 已於 db 建立 Language
$python manage.py migrate

#跑起來
python .\manage.py runserver

# 註冊 model languages\admin.py  
from .models import Language
admin.site.register(Language) 

=>之後可以在  localhost:8000/admin 的網頁看到 Language

#新增 laguages\serializers.py  : 轉 model  轉成 json (因為不能http直接傳 model 給人)
from django.db import models

class Language(models.Model):
	name = models.CharField(max_length=50)
	paradigm= models.CharField(max_length=50)


# 編輯 views.py
from django.shortcuts import render
from rest_framework import viewsets
from .models import Language
from .serializers import LanguageSerializer

class LanguageView(viewsets.ModelViewSet): 
	queryset = Language.objects.all()
	serializer_class = LanguageSerializer

 
# 編輯 languages\url.py
from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('languages', views.LanguageView)

urlpatterns = [
   path('', include(router.urls))
]

# 瀏覽 http://localhost:8000
http://localhost:8000/admin

# 用 postman 發發看
get http://localhost:8000/languages/

post http://localhost:8000/languages/
{"name": "C", "paradigm": "22"}

# router 會自己產生下面的model url 
http://localhost:8000/languages/2/

視頻最後三分鐘後面有說 model  加入 url , id 的方法 不重要所以沒加入
