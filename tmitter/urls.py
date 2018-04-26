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
import tmitter_web.views
import django.contrib.syndication.views
import django.conf.urls.i18n
from django.conf import settings
from django.conf.urls.static import static
from tmitter_web.feed import RSSRecentNotes,RSSUserRecentNotes

admin.autodiscover()

rss_feeds = {
    'recent': RSSRecentNotes,
}

rss_user_feeds = {
    'recent': RSSUserRecentNotes,
}

urlpatterns = [
    path('admin/', admin.site.urls),
# Example:
    # (r'^note/', include('note.foo.urls')),
    url(r'^$',tmitter_web.views.index),
    url(r'^p/(?P<_page_index>\d+)/$',tmitter_web.views.index_page,name="index_page"),
    url(r'^user/$',tmitter_web.views.index_user_self),
#    url(r'^user/(?P<_username>[a-zA-Z\-_\d]+)/$',tmitter.tmitter_web.views.index_user, name= "tmitter-mvc-views-index_user"),
    url(r'^user/(?P<_username>[a-zA-Z\-_\d]+)/$',tmitter_web.views.index_user, name="index_user"),
    url(r'^user/(?P<_username>[a-zA-Z\-_\d]+)/(?P<_page_index>\d+)/$',tmitter_web.views.index_user_page,name="index_user_page"),
    url(r'^users/$',tmitter_web.views.users_index),
    url(r'^users/(?P<_page_index>\d+)/$',tmitter_web.views.users_list,name="users_list"),
    url(r'^signin/$',tmitter_web.views.signin),
    url(r'^signout/$',tmitter_web.views.signout),
    url(r'^signup/$',tmitter_web.views.signup),
    url(r'^settings/$',tmitter_web.views.settings, name ='tmitter_mvc_views_settings'),
    url(r'^message/(?P<_id>\d+)/$',tmitter_web.views.detail, name="message_detail"),
    url(r'^message/(?P<_id>\d+)/delete/$',tmitter_web.views.detail_delete, name="message_delete"),
    url(r'^friend/add/(?P<_username>[a-zA-Z\-_\d]+)',tmitter_web.views.friend_add, name="friend_add"),
    url(r'^friend/remove/(?P<_username>[a-zA-Z\-_\d]+)',tmitter_web.views.friend_remove, name="friend_remove"),
    url(r'^api/note/add/',tmitter_web.views.api_note_add),
    url(r'^feed/rss/(?P<url>.*)/$', django.contrib.syndication.views.Feed, {'feed_dict': rss_feeds}),
    url(r'^user/feed/rss/(?P<url>.*)/$', django.contrib.syndication.views.Feed, {'feed_dict': rss_user_feeds}),
#    url(r'^static/(?P<path>.*)$', django.views.static.serve, {'document_root': settings.STATIC_ROOT}),
    url(r'^i18n/', django.conf.urls.i18n.i18n_patterns),
]
