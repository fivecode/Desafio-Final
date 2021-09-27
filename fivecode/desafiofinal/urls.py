"""desafiofinal URL Configuration

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
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings

from fivecode.views import home, form, create, view, edit, update, delete, formproduto, createproduto, deleteproduto, editarproduto,updateproduto
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name= "home"),
    path('empresa/novo/', form, name= "form"),
    path('create/', create, name= "create"),
    path('empresa/<int:pk_empresa>/produtos/', view, name="view"),
    path('empresa/<int:pk>/edit/', edit, name = "edit"),
    path('empresa/<int:pk>/update/', update, name = "update"),
    path ('empresa/<int:pk>/delete/', delete, name = "delete"),
    path('empresa/<int:pk_empresa>/produto/', formproduto, name= "formproduto"),
    path('createproduto/<int:pk_empresa>/', createproduto, name= "createproduto"),
    path('empresa/<int:pk_empresa>/produto/<int:pk>/delete/', deleteproduto, name= "deleteproduto"),
    path('empresa/<int:pk_empresa>/produto/<int:pk>/editar/', editarproduto, name= "editarproduto"),
    path('empresa/<int:pk_empresa>/produto/<int:pk>/update/', updateproduto, name= "updateproduto")        
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

