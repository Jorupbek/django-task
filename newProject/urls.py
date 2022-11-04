from allauth.account.views import ConfirmEmailView
from dj_rest_auth.registration.views import VerifyEmailView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('', include('api.urls')),
    path('api-auth/', include("rest_framework.urls")),
    path('rest-auth/', include("dj_rest_auth.urls")),
    path(
        'rest-auth/registration/account-confirm-email/<str:key>/',
        ConfirmEmailView.as_view(),
    ),
    path('rest-auth/registration/',
         include('dj_rest_auth.registration.urls')),
    path('rest-auth/account-confirm-email/',
         VerifyEmailView.as_view(),
         name='account_email_verification_sent'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
