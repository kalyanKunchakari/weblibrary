from django.shortcuts import render, redirect
from django.urls import reverse
from urllib.parse import urlencode
from django.http import HttpResponse
from . models import Student, Book, BookMainCategory, BookSubCategory, Book
from .forms import BookSubCategoryForm
# Create your views here.
def home(request):
    #return HttpResponse("home")
    st = Student.objects.all()
    context = {'st':st}
    return render(request, "dashboard.html", context)

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

