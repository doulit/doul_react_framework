from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('common/', include('common.urls')),                                            #공통

    # #계획표
    # path('planner/lectureSchedule/', include('planner.url.lectureSchedule_urls')),      #교수계획표(공학)


]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]

