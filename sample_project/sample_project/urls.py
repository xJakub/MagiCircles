from django.urls import include, re_path
from django.contrib import admin

handler500 = 'magi.views.handler500'
handler403 = 'magi.views.handler403'

urlpatterns = [
    # Examples:
    # re_path(r'^$', 'sample_project.views.home', name='home'),
    # re_path(r'^blog/', include('blog.urls')),

    re_path(r'^', include('magi.urls')),
    re_path(r'^admin/', admin.site.urls),
]
