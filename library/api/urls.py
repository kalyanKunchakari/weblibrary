from django.urls import path
from django.urls.resolvers import URLPattern
from library.api.views import api_detail_authorview, api_detail_bookview, api_detail_orderview, api_book_create, api_book_delete, api_detail_bookmodify, api_student_list, api_sub_category_list

app_name = 'library'

urlpatterns = [
    path("authors/<nm>/", api_detail_authorview),
    path("orders/<oid>/",api_detail_orderview),
    path("books/<bknm>", api_detail_bookview),
    path("books/update/<bknm>", api_detail_bookmodify),
    path("book/delete/<bknm>", api_book_delete),
    path("book/new/create", api_book_create),
    path("std_details/", api_student_list),
    path("subcat/<mc>/", api_sub_category_list)


]