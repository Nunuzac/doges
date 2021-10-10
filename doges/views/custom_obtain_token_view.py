from rest_framework_simplejwt.views import TokenObtainPairView
from doges.serializers import CustomTokenSerializer

class CustomObtainTokenView(TokenObtainPairView):
    serializer_class = CustomTokenSerializer