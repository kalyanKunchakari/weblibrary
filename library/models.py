from django.db import models

# Create your models here.
class Student(models.Model):
    STUDYING = (
                        ("Btech", "Btech"),
                        ("Mtech", "Mtech")
                        )
    BRANCH = (
                      ("CSE & IT", "CSE & IT"),
                      ("ECE", "ECE"),
                      ("EEE", "EEE"),
                      ("Mech", "Mech"),
                      ("Civil", "Civil")
                      )
    name = models.CharField(max_length=200, null=True)
    roll_num = models.CharField(max_length=200, null=True)
    studying = models.CharField(max_length=200, null=True, choices=STUDYING)
    branch = models.CharField(max_length=200, null=True, choices=BRANCH)
    pyr = models.IntegerField(null=True)
    
    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=200, null=True)
    
    def __str__(self):
        return self.name

class BookMainCategory(models.Model):
    category_name = models.CharField(max_length=20)
     
    def __str__(self):
        return self.category_name

class BookSubCategory(models.Model):
    sub_category_name = models.CharField(max_length=100)
    main_category = models.ForeignKey(BookMainCategory, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.sub_category_name    

class Book(models.Model):
    isbn_num = models.CharField("ISBN", max_length=20, help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')
    title = models.CharField(max_length=30, null=True)
    author = models.ForeignKey(Author,  on_delete=models.SET_NULL, null=True)
    summary = models.CharField(max_length=200, null=True)
    main_category = models.ForeignKey(BookMainCategory, on_delete=models.CASCADE, null=True)
    sub_category = models.ForeignKey(BookSubCategory, on_delete=models.CASCADE, null=True)
 
    def __str__(self):
        return self.title
    
        