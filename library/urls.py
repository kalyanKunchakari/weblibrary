from django.urls import include, path
from . import views

urlpatterns = [

	path("", views.home, name="home"),
	path("books/", views.books, name="books"),
    path("get_books", views.get_books, name="get_books"),
    path("load_subcats/", views.load_subCat, name="ajax_load_subcat")
]

