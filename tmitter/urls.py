"""tmitter URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url
from django.urls import path
from django.contrib import admin
import tmitter.mvc.views
import django.contrib.syndication.views
import django.conf.urls.i18n
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
# Example:
    # (r'^note/', include('note.foo.urls')),
    url(r'^$',tmitter.mvc.views.index),
    url(r'^p/(?P<_page_index>\d+)/$',tmitter.mvc.views.index_page),
    url(r'^user/$',tmitter.mvc.views.index_user_self),
#    url(r'^user/(?P<_username>[a-zA-Z\-_\d]+)/$',tmitter.mvc.views.index_user, name= "tmitter-mvc-views-index_user"),
    url(r'^user/(?P<_username>[a-zA-Z\-_\d]+)/$',tmitter.mvc.views.index_user, name= "tmitter-mvc-views-index_user"),
    url(r'^user/(?P<_username>[a-zA-Z\-_\d]+)/(?P<_page_index>\d+)/$',tmitter.mvc.views.index_user_page),
    url(r'^users/$',tmitter.mvc.views.users_index),
    url(r'^users/(?P<_page_index>\d+)/$',tmitter.mvc.views.users_list),
    url(r'^signin/$',tmitter.mvc.views.signin),
    url(r'^signout/$',tmitter.mvc.views.signout),
    url(r'^signup/$',tmitter.mvc.views.signup),
    url(r'^settings/$',tmitter.mvc.views.settings, name ='tmitter_mvc_views_settings'),
    url(r'^message/(?P<_id>\d+)/$',tmitter.mvc.views.detail, name = "tmitter-mvc-views-detail"),
    url(r'^message/(?P<_id>\d+)/delete/$',tmitter.mvc.views.detail_delete, name = "tmitter-mvc-views-detail_delete"),
    url(r'^friend/add/(?P<_username>[a-zA-Z\-_\d]+)',tmitter.mvc.views.friend_add, name="tmitter-mvc-views-friend_add"),
    url(r'^friend/remove/(?P<_username>[a-zA-Z\-_\d]+)',tmitter.mvc.views.friend_remove),
    url(r'^api/note/add/',tmitter.mvc.views.api_note_add),
    # Uncomment this for admin:
    #url(r'^admin/(.*)',admin.site.urls),
    url(r'^admin/',admin.site.urls),
    url(r'^feed/rss/(?P<url>.*)/$', django.contrib.syndication.views.Feed, {'feed_dict': rss_feeds}),
    url(r'^user/feed/rss/(?P<url>.*)/$', django.contrib.syndication.views.Feed, {'feed_dict': rss_user_feeds}),
#    url(r'^statics/(?P<path>.*)$', django.views.static.serve, {'document_root': settings.STATIC_ROOT}),
    url(r'^i18n/', django.conf.urls.i18n.i18n_patterns),
]+static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
