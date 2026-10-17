"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from ads import views
from ads.views import AdListView, AdCreateView, AdUpdateView, AdDeleteView
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login/', LoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(next_page='/'), name="logout"),
    path('', views.AdListView.as_view(), name="ad_list"),
    path('create/', views.AdCreateView.as_view(), name="create_ad"),
    path('<int:pk>/update/', views.AdUpdateView.as_view(), name="update_ad"),
    path('<int:pk>/delete/', views.AdDeleteView.as_view(), name="delete_ad"),
    path('<int:pk>/ad/', views.AdDetailView.as_view(), name="ad_details"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
