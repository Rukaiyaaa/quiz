
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user-register/', views.home, name='user_register'),
    path('user-login/', views.Userlogin, name='user_login'),
    path('account/', include('account.urls')),
    path('', include('quizes.urls')),
    path('', include('category.urls')),
    path('', include('questions.urls')),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)