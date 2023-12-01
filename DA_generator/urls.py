from django.urls import path
from . import views


urlpatterns = [
path("", views.index, name="index"),
# path("create_book/", views.BookCreate.as_view(), name="create_book"),
# path("book/<int:pk>/", views.BookDetail.as_view(), name="book_detail"),
path("script", views.script_page, name="script" ),
path("buyer-list", views.all_buyers, name= "buyer-list"),
path("order_DB", views.order_DB)

]