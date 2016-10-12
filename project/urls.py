from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^docs/', include('rest_framework_docs.urls')),
    url(r'', include("project.pages.urls", namespace="pages"))
]


urlpatterns += staticfiles_urlpatterns()
