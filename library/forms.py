from django.forms import ModelForm
from .models import BookSubCategory

class BookSubCategoryForm(ModelForm):
    class Meta:
        model = BookSubCategory
        fields = '__all__'