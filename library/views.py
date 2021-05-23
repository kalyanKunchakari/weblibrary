from django.shortcuts import render, redirect
from django.urls import reverse
from urllib.parse import urlencode
from django.http import HttpResponse
from . models import Student, Book, BookMainCategory, BookSubCategory, Book, StudentMainTable
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import BookForm, SignupForm1
from django.contrib import messages
from django import forms
# Create your views here.
def home(request):
    #return HttpResponse("home")
    st = Student.objects.all()
    context = {'st':st}
    return render(request, "dashboard.html", context)
'''
def books(request):
    form = BookSubCategoryForm()
    if request.method == "POST":
        print(request.POST)
        qs = request.POST
        form = BookSubCategoryForm(request.POST)
        if form.is_valid():
            #form.save()
            base_url = reverse("get_books")
            query_set = urlencode({"main_category":qs["main_category"][0], "sub_category":qs["sub_category_name"]})
            url = '{}?{}'.format(base_url, query_set)
            return redirect(url)
            
    context = {"form":form}    
    return render(request, "books.html", context)

def get_books(request):
    main_category_id = request.GET.get("main_category")
    sub_category = request.GET.get("sub_category")
    mc = BookMainCategory.objects.get(id=main_category_id)
    print(mc)
    print(sub_category)
    fb =   Book.objects.filter(main_category=mc).filter(sub_category__sub_category_name=sub_category)
    print(fb)
    context = {"fb":fb}
    return render(request, "get_books.html", context)

'''
def signup_form(request):

    if request.method == 'POST':
        form = SignupForm1(request.POST)
        if form.is_valid():
            rn = form.cleaned_data.get("rollNumber")
            un = form.cleaned_data.get("username")
            #print(rn)
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
            user.save()

            messages.success(request, "Account created successfully for "+ user.student.name)
            return redirect("login")
        #    else:
        #        raise forms.ValidationError("The roll number doesnt exists")            
    else:
        form = SignupForm1()
    return render(request, "signup.html", {'form': form})       
    
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

def books(request):
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
            context = {"fb":fb, "form":form1}
            return render(request, "books.html", context)
    else:       
        context = {"form":form1}    
        return render(request, "books.html", context)

def get_books(request):
    form = BookForm()
    main_category_id = request.GET.get("main_category")
    sub_category1 = request.GET.get("sub_category")
    mc = BookMainCategory.objects.get(id=main_category_id)
    sc = BookSubCategory.objects.get(id=sub_category1)
    fb =   Book.objects.filter(main_category=mc).filter(sub_category__sub_category_name=sc)
    context = {"fb":fb, "form":form}
    return render(request, "books.html", context)
 
def load_subCat(request):
    main_id = request.GET.get("main_cat")
    subCats = BookSubCategory.objects.filter(main_category_id = main_id)
    return render(request, "subCat_dropdown_list.html", {'subCats': subCats})    
