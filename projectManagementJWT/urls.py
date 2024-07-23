from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from PROJECTS.views import ProjectViewSet, TaskViewSet, ProjectUserViewSet, UserViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register(r'projects', ProjectViewSet)
router.register(r'tasks', TaskViewSet)
router.register(r'project-User', ProjectUserViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/users/', UserViewSet.as_view({'get': 'list', 'post': 'create'}), name='user'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
