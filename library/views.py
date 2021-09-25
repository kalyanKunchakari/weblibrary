from django.http.response import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from urllib.parse import urlencode
from django.http import HttpResponse
from . models import Student, Book, BookMainCategory, BookSubCategory, Book, StudentMainTable, Order
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group, User
from django.contrib.auth.decorators import login_required
from .forms import BookForm, SignupForm1, CreateBook, DeleteBook
from django.contrib import messages
from django import forms
from django.views import generic
from .decorators import unauthenticated_user, allowed_user

import json
# Create your views here.
@login_required(login_url="login")
@allowed_user(allowed_role=['admin'])
def home(request):
    #return HttpResponse("home")
    st = Student.objects.all()
    context = {'st':st}
    return render(request, "dashboard.html", context)

@unauthenticated_user
def signup_form(request):

    if request.method == 'POST':
        form = SignupForm1(request.POST)

        if form.is_valid():
            rn = form.cleaned_data.get("rollNumber")
            un = form.cleaned_data.get("username")
            print(rn)
            print(un)
            #print(StudentMainTable.objects.filter(stdid=rn))
                #if StudentMainTable.objects.filter(stdid=rn).exists() :
                #    if User.objects.filter(username=un).exists():
                #       raise forms.ValidationError("User already exists")
                #    else:    
            user = form.save()

            user.refresh_from_db()
            user.student.name = form.cleaned_data.get('username')
            user.student.roll_num = form.cleaned_data.get('rollNumber')
            user.student.studying = form.cleaned_data.get('studying')
            user.student.branch = form.cleaned_data.get('branch')
            user.student.pyr = form.cleaned_data.get('persuingyear')
            group = Group.objects.get(name="student")
            user.groups.add(group)
            user.save()

            messages.success(request, "Account created successfully for "+ user.student.name)
            return redirect("login")
        #    else:
        #        raise forms.ValidationError("The roll number doesnt exists")            
    else:
        form = SignupForm1()
    return render(request, "signup.html", {'form': form})       

@unauthenticated_user
def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.info(request, "Username or password is incorrect")
    return render(request, "login.html")

def logoutUser(request):
    logout(request)
    return redirect("login")    

@login_required(login_url="login")
def books(request):
    std_details = Student.objects.filter(name=request.user)
    form1 = BookForm()
    if request.method == "POST":
        print(request.POST)
        qs = request.POST
        form = BookForm(request.POST)
        if form.is_valid():
            #form.save()
            #base_url = reverse("get_books")
            main_category_id = qs["main_category"] 
            sub_category1 = qs["sub_category"]
            #url = '{}?{}'.format(base_url, query_set)
            print(main_category_id)
            print(sub_category1)
            mc = BookMainCategory.objects.get(id=main_category_id)
            sc = BookSubCategory.objects.get(id=sub_category1)
            fb =   Book.objects.filter(main_category=mc).filter(sub_category__sub_category_name=sc)
            context = {"fb":fb, "form":form1, "std_details":std_details}
            return render(request, "books.html", context)
    else:       
        context = {"form":form1, "std_details":std_details}    
        return render(request, "books.html", context)

def load_subCat(request):
    main_id = request.GET.get("main_cat")
    subCats = BookSubCategory.objects.filter(main_category_id = main_id)
    return render(request, "subCat_dropdown_list.html", {'subCats': subCats})

def signup_ajax(request):
    rollNum = request.GET.get("roll_num")
    std_details = StudentMainTable.objects.filter(stdid=rollNum)
    #print(std_details)
    reslt = {}
    if std_details:
        for std in std_details:
            if std.name and std.email_id and std.degree and std.branch and std.persuing_year:
                print(std.name)
                reslt['name'] = std.name
                reslt['email_id'] = std.email_id
                reslt['degree'] = std.degree
                reslt['branch'] = std.branch
                reslt['persuing_year'] = std.persuing_year
    print(reslt['name'])
    r = JsonResponse(reslt)
    print(r)            
    return JsonResponse(reslt)

#class BookDetailedView(generic.DetailView):
#    model = Book
@login_required(login_url="login")
def book_detail_view(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'book_detail.html', context={'book': book})

@login_required(login_url="login")
def book_orders(request):
    book_name = request.GET.get("book_name")
    print(book_name)
    
    std = Student.objects.get(user=request.user)
    print(std)
    bk = Book.objects.get(title = book_name)
    add_item = True
    try:
        ordrs = std.order_set.all()
        if ordrs:
            for ord in ordrs:
                if ord.book.id == bk.id:
                    add_item = False
                    break
        if add_item:
            Order.objects.create(std=std, book = bk)
            bk.book_count = bk.book_count - 1
            bk.save()
        else:
            return JsonResponse({'msg': "Maximum of 1 copy of book is allowed to order "})    
    except Exception as e:
        return JsonResponse({'msg':"Failed to add the order to the cart." })
    return JsonResponse({'msg': "Order added to the cart successfully."})

@login_required(login_url="login")
def student_orders(request):
    std = Student.objects.get(user=request.user)
    ordered_books = std.order_set.all()
    print(ordered_books)
    return render(request, "studentOrders.html", context={"ordered_books": ordered_books})

@login_required(login_url="login")
@allowed_user(allowed_role=['admin'])
def AddBook(request):
    std_details = Student.objects.filter(name=request.user)
    form = CreateBook()
    print(request.method)
        
    if request.method == "POST":
        
        form = CreateBook(request.POST)
        if form.is_valid():
            form.save()
        else:
            return JsonResponse({'msg': "Failed to add book "})
    else:       
        context = {"form":form, "std_details":std_details}    
        return render(request, "create_book.html", context)
    return JsonResponse({'msg': "Book Added successfully."})

@login_required(login_url="login")
@allowed_user(allowed_role=['admin'])
def RemoveBook(request):
    form = DeleteBook()
    if request.method == "POST":
        qs = request.POST
        form = DeleteBook(request.POST)
        if form.is_valid():
            title = qs['title']
            bk = Book.objects.get(title=title)
            bk.delete()
            
        else:
            return HttpResponse("Failed to remove book ")
    else:       
        context = {"form":form}    
        return render(request, "delete_book.html", context)
    return HttpResponse("Book Deleted successfully.")

        


