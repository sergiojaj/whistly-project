from django.urls import path

# func based views
# class based views
from .views import (
    AddBirdCreateView,
    BirdDeleteView,
    BirdDetailSimpleView,
    BirdsNestListView,
    BirdUpdateView,
    CustomPasswordChangeView,
    EditCommentUpdateView,
    EditReplyUpdateView,
    HomeTemplateView,
    ProfileDetailView,
    ProfileUpdateView,
    RemoveAccountDeleteView,
    SearchResultsListView,
    Seed_Add_Remove_View,
    approve_comment,
    approve_reply,
    remove_comment,
    remove_reply,
)

urlpatterns = [
    # basic urls
    path("", HomeTemplateView.as_view(), name="home"),
    path(
        "remove_account/<uuid:pk>/",
        RemoveAccountDeleteView.as_view(),
        name="remove_account",
    ),
    # profile urls
    path(
        "user_profile/<uuid:pk>/edit/",
        ProfileUpdateView.as_view(),
        name="edit_profile",  # noqa: E501
    ),
    path(
        "user_profile/<uuid:pk>/",
        ProfileDetailView.as_view(),
        name="profile_detail",  # noqa: E501
    ),  # noqa: E501
    path(
        "accounts/password/change/",
        CustomPasswordChangeView.as_view(),
        name="account_change_password",
    ),
    # bird urls
    path("feathers_up/", AddBirdCreateView.as_view(), name="add_bird"),  # noqa: E501
    path("birds_nest/", BirdsNestListView.as_view(), name="birds_nest"),  # noqa: E501
    path(
        "birds_nest/<uuid:pk>/",
        BirdDetailSimpleView.as_view(),
        name="bird_detail",  # noqa: E501
    ),  # noqa: E501
    path(
        "birds_nest/<uuid:pk>/edit/",
        BirdUpdateView.as_view(),
        name="bird_update",  # noqa: E501
    ),  # noqa: E501
    path(
        "birds_nest/<uuid:pk>/delete/",
        BirdDeleteView.as_view(),
        name="bird_delete",  # noqa: E501
    ),  # noqa: E501
    # comments
    path(
        "birds_nest/<uuid:pk>/comment_approved/",
        approve_comment,
        name="comment_approved",
    ),
    path(
        "birds_nest/<uuid:pk>/comment_removed/",
        remove_comment,
        name="comment_removed",  # noqa: E501
    ),
    path(
        "birds_nest/<uuid:pk>/edit_comment/",
        EditCommentUpdateView.as_view(),
        name="comment_edit",
    ),
    # replies
    path(
        "birds_nest/<uuid:pk>/reply_approved/",
        approve_reply,
        name="reply_approved",  # noqa: E501
    ),  # noqa: E501
    path(
        "birds_nest/<uuid:pk>/reply_removed/",
        remove_reply,
        name="reply_removed",  # noqa: E501
    ),  # noqa: E501
    path(
        "birds_nest/<uuid:pk>/edit_reply/",
        EditReplyUpdateView.as_view(),
        name="reply_edit",
    ),
    # seeds
    # path('birds_nest/<uuid:pk>/seed', add_remove_seed_function_view, name='seed'),  # noqa: E501
    path(
        "birds_nest/<uuid:pk>/seed",
        Seed_Add_Remove_View.as_view(),
        name="seed",  # noqa: E501
    ),  # noqa: E501
    # search
    path(
        "search/", SearchResultsListView.as_view(), name="search_results"
    ),  # noqa: E501
]
