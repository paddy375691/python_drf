"""devops_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from libs.token_auth import CustomAuthToken, ChangeUserPasswordView
from cmdb.views import HostCollectView

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('^api/login/$', CustomAuthToken.as_view()),
    re_path('^api/change_password/$', ChangeUserPasswordView.as_view()),
    re_path('^api/cmdb/host_collect/$', HostCollectView.as_view()),
]

# CMDB
from cmdb.views import IdcViewSet, ServerGroupViewSet, ServerViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'cmdb/idc', IdcViewSet, basename="idc")
router.register(r'cmdb/server_group', ServerGroupViewSet, basename="server_group")
router.register(r'cmdb/server', ServerViewSet, basename="server")

# 凭据
from system_config.views import CredentialViewSet
router.register(r'config/credential', CredentialViewSet, basename='credential')

urlpatterns += [
    path('api/', include(router.urls))
]