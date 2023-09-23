from django.urls import path
from .views import ProfilesView, ProfileView

urlpatterns = [
    path('', ProfilesView.as_view()),
    path('<uuid:profile_id>/', ProfileView.as_view()),
    # ping endpoing
    path('ping/', lambda request: HttpResponse('pong')),
]
