from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, CategoryViewSet, login_view, logout_view, CustomTokenObtainPairView, CustomTokenRefreshView

# Créez un routeur et enregistrez les ViewSets
router = DefaultRouter()
router.register(r'books', BookViewSet)
router.register(r'categories', CategoryViewSet)

urlpatterns = [
    # Endpoints API
    path('', include(router.urls)),  # Inclure les routes API générées par le routeur
    path('login/', login_view, name='api_login'),  # Endpoint pour obtenir le token JWT
    path('logout/', logout_view, name='api_logout'),  # Endpoint pour mettre le token de rafraîchissement en liste noire
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),  # Endpoint pour obtenir le token JWT
    path('token/refresh/', CustomTokenRefreshView.as_view(), name='token_refresh'),  # Endpoint pour rafraîchir le token JWT
]
