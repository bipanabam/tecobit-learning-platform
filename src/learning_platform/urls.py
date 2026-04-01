from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from . import views

from emails.views import verify_email_token_view, email_token_signup_view, logout_hx_view

urlpatterns = [
    path("", views.homepage, name="home"),
    path("signup/", email_token_signup_view, name='signup'),
    # path("hx/signup/", email_token_signup_view, name="hx_signup"),
    path("hx/logout/", logout_hx_view, name="hx_logout"),
    path("verify/<uuid:token>/", verify_email_token_view, name='verify_token'),
    path('admin/', admin.site.urls),
    path("auth/", include('users.urls')),
    path("courses/", include('courses.urls')),
]

if settings.DEBUG:
    urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += path("__reload__/", include("django_browser_reload.urls")),

