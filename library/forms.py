from django.forms import ModelForm
from .models import BookSubCategory, Book, StudentMainTable
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError
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
'''
class SignupForm(UserCreationForm):
    rollNumber = forms.CharField(max_length=200, help_text="Roll Number of the student", widget=forms.TextInput(attrs={'placeholder': 'Roll Number'}))
    name = forms.CharField(max_length=200, help_text= "Name of the student", widget=forms.TextInput(attrs={'placeholder': 'Student Name'}))
    studying = forms.CharField(max_length=200, help_text="Degree of the student", widget=forms.TextInput(attrs={'placeholder': 'Degree'}))
    branch = forms.CharField(max_length=200, help_text="Branch of the student", widget=forms.TextInput(attrs={'placeholder': 'Branch'}))
    persuingyear = forms.IntegerField(help_text="Persuing year fo the student", widget=forms.TextInput(attrs={'placeholder': 'pursuing year'}))
    email = forms.EmailField(max_length=100, help_text="Student email", widget=forms.TextInput(attrs={'placeholder': 'Email Address'}))
    class Meta:
        model = User
        fields = ('rollNumber', 'name',  'studying', 'branch', 'persuingyear', 'email', 'password1', 'password2')

'''
class SignupForm1(UserCreationForm):
    rollNumber = forms.CharField(max_length=200, help_text="Roll Number of the student", widget=forms.TextInput(attrs={'placeholder': 'Roll Number'}))
    username = forms.CharField(max_length=200, help_text= "Name of the student", widget=forms.TextInput(attrs={'placeholder': 'Student Name'}))
    studying = forms.CharField(max_length=200, help_text="Degree of the student", widget=forms.TextInput(attrs={'placeholder': 'Degree'}))
    branch = forms.CharField(max_length=200, help_text="Branch of the student", widget=forms.TextInput(attrs={'placeholder': 'Branch'}))
    persuingyear = forms.IntegerField(help_text="Persuing year fo the student", widget=forms.TextInput(attrs={'placeholder': 'pursuing year'}))
    email = forms.EmailField(max_length=100, help_text="Student email", widget=forms.TextInput(attrs={'placeholder': 'Email Address'}))
    class Meta:
        model = User
        fields = ('rollNumber', 'username',  'studying', 'branch', 'persuingyear', 'email', 'password1', 'password2')
        #fields = ('username', 'email', 'password1', 'password2')
    def clean_rollNumber(self):
        rollnum = self.cleaned_data.get("rollNumber")
        un = self.cleaned_data.get("username")
        print(un)
        print(rollnum)
        rnqs = StudentMainTable.objects.filter(stdid=rollnum)
        print(rnqs)
        if rnqs.exists() :
            for obj in rnqs:
                nm = obj.name
            if nm == un:    
                return rollnum
            else:
                raise forms.ValidationError("User name mismatch. The specified roll number has different user name")            
        else:
            raise forms.ValidationError("The roll number doesnt exist in the main db")     
            
        
        
        