from dj_rest_auth.registration.views import VerifyEmailView
from django.urls import path, re_path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.routers import SimpleRouter, DefaultRouter

from author.views import AuthorViewSet, GenreViewSet
from book.views import BookViewSet, ReviewViewSet

schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@contact.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

router = DefaultRouter()
router.register("book", BookViewSet, basename="book")
router.register("review", ReviewViewSet, basename="review")
router.register("author", AuthorViewSet, basename="author")
router.register("genre", GenreViewSet, basename="genre")

urlpatterns += router.urls
