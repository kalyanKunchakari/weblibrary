from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import SET_NULL
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse
# Create your models here.
class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, null=True)
    roll_num = models.CharField(max_length=200, null=True)
    studying = models.CharField(max_length=200, null=True)
    branch = models.CharField(max_length=200, null=True)
    pyr = models.CharField(max_length=200,null=True)

    def __str__(self):
        return str(self.user.username)
    
    @receiver(post_save, sender=User)
    def create_student(sender, instance, created, **kwargs):
        if created:
            Student.objects.create(user=instance)
        instance.student.save()     
    
    

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

class StudentMainTable(models.Model):
    stdid = models.AutoField(primary_key=True, blank=True)
    name = models.TextField()
    email_id = models.TextField(blank=True, null=True)
    degree = models.TextField()
    branch = models.TextField()
    persuing_year = models.TextField()
    doj = models.TextField()

    class Meta:
        managed = False
        db_table = 'student'
    def __str__(self):
        return self.name    
        
class Book(models.Model):
    isbn_num = models.CharField("ISBN", max_length=20, help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')
    title = models.CharField(max_length=100, null=True)
    author = models.ForeignKey(Author,  on_delete=models.SET_NULL, null=True)
    summary = models.CharField(max_length=200, null=True, blank=True)
    main_category = models.ForeignKey(BookMainCategory, on_delete=models.CASCADE, null=True)
    sub_category = models.ForeignKey(BookSubCategory, on_delete=models.CASCADE, null=True)
    book_count = models.IntegerField(null=False, default=0)
 
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book-detail', args=[str(self.id)])

class Order(models.Model):
    order_id = models.AutoField(primary_key=True)   
    std = models.ForeignKey(Student, null=True, on_delete=SET_NULL)
    book = models.ForeignKey(Book, null=True, on_delete=SET_NULL)
    date_created = models.DateField(auto_now_add=True, null=True)

    def __str__(self):
        return str(self.order_id)
