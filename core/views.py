from rest_framework import permissions
from rest_framework.generics import CreateAPIView, ListAPIView
from drf_yasg import openapi as drf_yasg_openapi
from drf_yasg import views as drf_yasg_views
from core.models import Home, Request, HomeType, Type
from core.serializers import HomeSerializer, RequestSerializer, HomeTypeSerializer, TypeSerializer

schema_view = drf_yasg_views.get_schema_view(
    drf_yasg_openapi.Info(
        title="Abbos API",
        default_version="v1",
        # description="Test description",
        # terms_of_service="https://www.google.com/policies/terms/",
        contact=drf_yasg_openapi.Contact(url="https://t.me/Algorithm_gateway_T"),
        license=drf_yasg_openapi.License(name="Proprietary software license"),
    ),
    public=False,
    permission_classes=(permissions.AllowAny,),
)
class HomeTypeView(ListAPIView):
    serializer_class = HomeTypeSerializer
    queryset = HomeType.objects.all()


class TypeView(ListAPIView):
    serializer_class = TypeSerializer
    queryset = Type.objects.all()


class HomeView(CreateAPIView):
    serializer_class = HomeSerializer
    queryset = Home.objects.all()


class RequestView(CreateAPIView):
    serializer_class = RequestSerializer
    queryset = Request.objects.all()

