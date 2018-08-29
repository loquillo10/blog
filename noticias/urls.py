from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
<<<<<<< HEAD

    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('blog.urls')),
=======
    # Examples:
    #url(r'^$', 'noticias.views.home', name='home'),
    #url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
>>>>>>> 549e2eaa79a933393455487062890038fa17791a
]
