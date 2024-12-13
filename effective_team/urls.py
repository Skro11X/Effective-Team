from django.urls import path
from effective_team.views import RotateScoreAPIView, CreatorViewSet, MemberViewSet, TeamViewSet, TeamApplicationViewSet
from drf_spectacular.views import SpectacularSwaggerView, SpectacularAPIView
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'creator', CreatorViewSet)
router.register(r'member', MemberViewSet)
router.register(r'team', TeamViewSet)
router.register(r'team-application', TeamApplicationViewSet)

urlpatterns = router.urls + [
    path('rotate_score/', RotateScoreAPIView.as_view(), name='rotate_score'),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('shema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui')
]