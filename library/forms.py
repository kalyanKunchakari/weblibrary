from django.forms import ModelForm
from .models import BookSubCategory, Book
'''
class BookSubCategoryForm(ModelForm):
    class Meta:
        model = BookSubCategory
        fields = '__all__'
     
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['sub_category_name'].queryset = BookSubCategory.objects.none()
'''        
class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = {'main_category', 'sub_category'}
     
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['sub_category'].queryset = BookSubCategory.objects.none()
        
        if 'main_category' in self.data:
            try:
                main_category_id = int(self.data.get('main_category'))
                self.fields['sub_category'].queryset = BookSubCategory.objects.filter(main_category_id=main_category_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['sub_category'].queryset = self.instance.main_category.sub_category_set.order_by('name')
           