from django.urls import path
from EffectiveTeam.views import CreatorAPIView, TeamAPIView, MemberAPIView, TeamApplicationAPIView, RotateScoreAPIView
from drf_spectacular.views import SpectacularSwaggerView, SpectacularAPIView


urlpatterns = [
    path('creator/<int:pk>/', CreatorAPIView.as_view(), name='creator'),
    path('member/<int:pk>/', MemberAPIView.as_view(), name='member'),
    path('team/<int:pk>/', TeamAPIView.as_view(), name='team'),
    path('team_application/', TeamApplicationAPIView.as_view(), name='teamApplication'),
    path('rotate_score/', RotateScoreAPIView.as_view(), name='rotate_score'),
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path('shema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui')
]