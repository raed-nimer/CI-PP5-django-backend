from django.urls import path
from django.http import HttpResponse
from .views import RegisterView, LoginView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
path('register', RegisterView.as_view(), name='signup'),
path('login', LoginView.as_view(), name='login'),
]

# urlpatterns += static(
#         settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)