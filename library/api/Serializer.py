from django.db.models import fields
from rest_framework import serializers, permissions
from library.models import Author, Order, Book, Student, BookMainCategory, BookSubCategory

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['name']

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['order_id', 'std', 'book']

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ["isbn_num", "title", "author", "summary", "book_count"]

class StudentSerializer(serializers.ModelSerializer):
    books_ordered = serializers.SerializerMethodField("get_book_count")
    class Meta:
        model = Student
        fields = '__all__'

    def get_book_count(self, std):
        books_ordered = std.order_set.all().count()
        return books_ordered
'''
class MainCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BookMainCategory
        fields = "__all__"
'''
class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BookSubCategory
        fields = ["sub_category_name"]

