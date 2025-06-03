from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.logocover, name='logocover'),  # Landing page
    path('home/', views.home, name='home'),  # About Us page
    path('login/', views.login_register_view, name='login'),  # Login/Register page
    path('index/', views.index, name='index'),  # Dashboard for general users
    path('general-discussion/', views.general_discussion, name='general_discussion'),
    path('map/', views.map_view, name='map'),
    path('support/', views.support, name='support'),
    path('logout/', auth_views.LogoutView.as_view(next_page='logocover'), name='logout'),
    path('video/', views.video_tutorials, name='video_tutorials'),
    path('help-line/', views.help_line, name='help_line'),

    # Story pages
    path('story/', views.story_view, name='story'),
    path('story1/', views.story_view1, name='story1'),
    path('story2/', views.story_view2, name='story2'),
    path('story3/', views.story_view3, name='story3'),
    path('story4/', views.story_view4, name='story4'),
    path('story5/', views.story_view5, name='story5'),
    path('story6/', views.story_view6, name='story6'),
    path('story7/', views.story_view7, name='story7'),
    path('story8/', views.story_view8, name='story8'),
    path('story9/', views.story_view9, name='story9'),
    path('story10/', views.story_view10, name='story10'),

    # Reporting
    path('send-report/', views.report_incident, name='report_incident'),
    path('report/', views.report_issue, name='report_issue'),

    # Admin-only dashboard (restricted in view)
    path('admin-dashboard/', views.user_dashboard, name='user_dashboard'),
]

# Serve uploaded media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
