from django.urls import path
from . import views

urlpatterns = [
    path("", views.BookView.as_view(), name="book_list"),
    path("publishers/", views.PublisherView.as_view(), name="publisher_list"),
    path("reviews/", views.ReviewView.as_view(), name="review_list"),
]
