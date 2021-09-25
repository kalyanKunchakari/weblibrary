from rest_framework import serializers, status, permissions
from rest_framework import response
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes

from library.models import Author, BookSubCategory, Order, Book, StudentMainTable, Student, BookMainCategory
from library.api.Serializer import AuthorSerializer, OrderSerializer, BookSerializer, StudentSerializer, SubCategorySerializer

@api_view(['GET',])
@permission_classes((permissions.AllowAny,))
def api_detail_authorview(request, nm):
    try:
        athr = Author.objects.get(name=nm)
    except Author.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        serializer = AuthorSerializer(athr)
        return Response(serializer.data)

@api_view(['GET',])
@permission_classes((permissions.AllowAny,))
def api_detail_orderview(request, oid):
    try:
        ordr = Order.objects.get(order_id = oid)
    except Order.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        srl = OrderSerializer(ordr)
        return Response(srl.data)

@api_view(['GET',])
@permission_classes((permissions.AllowAny,))
def api_detail_bookview(request, bknm):
    try:
        bk = Book.objects.get(title = bknm)
    except Book.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        bk_srl = BookSerializer(bk)
        return Response(bk_srl.data)

@api_view(['PUT',])
@permission_classes((permissions.AllowAny,))
def api_detail_bookmodify(request, bknm):
    try:
        bk = Book.objects.get(title = bknm)
    except Book.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'PUT':
        bk_srl = BookSerializer(bk, data=request.data)
        data = {}
        if bk_srl.is_valid():
            bk_srl.save()
            data['Success'] = "Update successful"
            return Response(data=data)
        return Response(bk_srl.errors, status=status.HTTP_400_BAD_REQUEST)    
        
@api_view(['DELETE',])
@permission_classes((permissions.AllowAny,))
def api_book_delete(request, bknm):
    try:
        bk = Book.objects.get(title = bknm)
    except Book.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == "DELETE":
        opr = bk.delete()
        data = {}
        if opr:
            data['Success'] = "Object deleted successfully"
        else:
            data['Failure'] = "Object delete failed"
        return Response(data=data)

@api_view(['POST',])
@permission_classes((permissions.AllowAny,))
def api_book_create(request):
    try:
        author = Author.objects.get(pk=11)
        bkc = Book(author=author)
        if request.method == "POST":
            bk_srl = BookSerializer(bkc, data=request.data)
            if bk_srl.is_valid():
                bk_srl.save()
                return Response(bk_srl.data, status=status.HTTP_201_CREATED)
            return Response(bk_srl.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        print(e)

@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def api_student_list(request):
    std_dts = Student.objects.all()
    std = StudentSerializer(std_dts, many=True)
    return Response(std.data)
'''
@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def api_main_category_list(request):
    main_lst = BookMainCategory.objects.all()
    main_slr = MainCategorySerializer(main_lst, many=True)
    return Response(main_slr.data)
'''
@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def api_sub_category_list(request, mc):
    sub_cat = BookSubCategory.objects.filter(main_category_id = mc)
    sub_slr = SubCategorySerializer(sub_cat, many=True)
    return Response(sub_slr.data)



            
                