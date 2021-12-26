from django.conf.urls import include, url
from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.main_page),
    path('register/', views.register),
    path('logout/', views.logout_reqest),
     path('login/', views.login_reqest)

]

urlpatterns+= static(settings.STATIC_URL,
                     document_root=settings.STATIC_ROOT)
print (urlpatterns)