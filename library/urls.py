from django.urls import include, path
from . import views

urlpatterns = [

	path("", views.home, name="home"),
	path("books/", views.books, name="books"),
    #path("books", views.get_books, name="get_books"),
    path("load_subcats/", views.load_subCat, name="ajax_load_subcat"),
    path("signup/", views.signup_form, name="signup"),
    path("login/", views.login_page, name="login"),
    path("logout/", views.logoutUser, name="logout"),
    path('signup_ajax', views.signup_ajax, name="signup_ajax"),
    path('book/<int:pk>', views.book_detail_view, name="book-detail"),
    path('orders/', views.book_orders, name="ajax_orders"),
    path('student_orders/', views.student_orders, name="student_orders"),
    path('create_book/', views.AddBook, name="create_book"),
    path('delete_book/', views.RemoveBook, name="delete_book")
]

