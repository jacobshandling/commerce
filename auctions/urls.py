from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("new-listing", views.new_listing, name="new-listing"),
    path("listing/<int:listing_id>", views.listing, name="listing"),
    path("watchlist-action", views.watchlist_action, name="watchlist-action"),
    # path("watch", views.un_watch, {"watch":True}, name="watch")
]
