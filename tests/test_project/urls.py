from django.urls import include, re_path
from django.contrib import admin

urlpatterns = [
    # Examples:
    # re_path(r'^$', 'test_project.views.home', name='home'),
    # re_path(r'^blog/', include('blog.urls')),

    re_path(r'^', include('magi.urls')),
    re_path(r'^admin/', admin.site.urls),
]
